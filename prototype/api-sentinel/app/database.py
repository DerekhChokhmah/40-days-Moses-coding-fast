from sqlalchemy import create_engine, select, exc, text
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from models import Base, Monitor, MonitoringResult
from http_monitor import httpEngine
import os 
import redis
from celery import Celery
postgresql_db_password = os.environ["postgresql_db_password"]
                        #address of the db                    

app = Celery('check_monitor',broker="redis://localhost:6379/0")
                      
engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql          

Base.metadata.create_all(engine)
Session = sessionmaker(engine)

@app.task
def check_monitor(monitor_id):
   with Session() as session:
     result_mon_with_id = find_monitor(monitor_id, session)
     final_result_with_id = monitoring_results(result_mon_with_id, session)
     monitoring_result_output(final_result_with_id)
     

@app.on_after_configure.connect
def setup_periodic_task(sender: Celery, **kwargs):
    with Session() as session:
        result = find_active_monitors(session)
        for mon in result:
            sender.add_periodic_task(mon.interval_value, check_monitor.s(mon.id), name='add every {}s'.format(mon.interval_value))   

   
def monitoring_results(monitor, session):
      monitoring_result = httpEngine(monitor)
      session.add(monitoring_result)
      session.commit()
      return monitoring_result
   
def monitoring_result_output(results_mon):
    print(results_mon.id, results_mon.monitor_id, results_mon.status_code, results_mon.response_time, results_mon.success, results_mon.checked_at)
    #print(r.hgetall(key))

    
def find_monitor(monitor_id, session):
    r = redis.Redis(host="localhost", port=6379, decode_responses=True)
    key = "monitor:{}".format(monitor_id)
    redis_result = r.hgetall(key)
    if redis_result:
       Id = int(redis_result["id"])
       if redis_result["active"] == "True":
          Active = True
       else:
          Active = False
       exp_status = int(redis_result["expected_status"])
       inter_value =  int(redis_result["interval_value"])    
       monitor = Monitor(id=Id, name=redis_result["name"], url=redis_result["url"], active=int(Active), method=redis_result["method"], expected_status=exp_status, interval_value=inter_value)  
       return monitor
         
    
   
    else:
      stmt = select(Monitor).where(Monitor.id == monitor_id)
      result = session.execute(statement=stmt)
      mon = result.scalars().all()
    if not mon:
            print(NoResultFound)
    else:  
            for monitor in mon:
              maps = {
              "id": monitor.id,
              "name":monitor.name,
              "url":monitor.url,
              "active":int(monitor.active),
              "method":monitor.method,
              "expected_status":monitor.expected_status,
              "interval_value":monitor.interval_value
            }
              r.hset(key, mapping=maps)
              return monitor


def find_active_monitors(session):
    stmt = select(Monitor).where(Monitor.active == True)
    result = session.execute(stmt)
    return result.scalars().all()
        



    

