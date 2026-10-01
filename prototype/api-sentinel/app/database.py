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
r = redis.Redis(host="localhost", port=6379, decode_responses=True)
app = Celery('hello',broker="redis://localhost:6379/0")
@app.task
def hello():
    return "Hi"                       
'''engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql 
key = "monitor:1"          
redis_result = r.hgetall(key)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
stmt = select(Monitor).where(Monitor.id == 1)

def monitoring_results(monitor, session):
      monitoring_result = httpEngine(monitor)
      session.add(monitoring_result)
      session.commit()
      return monitoring_result
   
def monitoring_result_output(results_mon):
    print(results_mon.id, results_mon.monitor_id, results_mon.status_code, results_mon.response_time, results_mon.success, results_mon.checked_at)
    print(r.hgetall(key))
if redis_result:
   Id = int(redis_result["id"])
   if redis_result["active"] == "True":
      Active = True
   else:
      Active = False
   exp_status = int(redis_result["expected_status"])
   inter_value =  int(redis_result["interval_value"])    
   with Session() as session:
      monitor = Monitor(id=Id, name=redis_result["name"], url=redis_result["url"], active=int(Active), method=redis_result["method"], expected_status=exp_status, interval_value=inter_value)  
      result_mon = monitoring_results(monitor,session)
      monitoring_result_output(result_mon)
    
   
else:
  with Session() as session:
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
          result_mon = monitoring_results(monitor, session)
          monitoring_result_output(result_mon)
                  
    
    

         
           
'''