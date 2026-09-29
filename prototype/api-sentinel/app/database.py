from sqlalchemy import create_engine, select, exc, text
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from models import Base, Monitor, MonitoringResult
from http_monitor import httpEngine
import os 
import redis
postgresql_db_password = os.environ["postgresql_db_password"]
                        #address of the db
r = redis.Redis(host="localhost", port=6379, decode_responses=True)                    
engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql 
key = "monitor:5"          
redis_result = r.hgetall(key)
if redis_result:
   print(redis_result)
else:
  Base.metadata.create_all(engine)
  Session = sessionmaker(engine)
#with Session() as session:
#    session.add()
#    session.commit() 
  stmt = select(Monitor).where(Monitor.id == 5)
  stmt_res = select(MonitoringResult)
  with Session() as session:
    #monitor_1 = Monitor(id=1, name="GITHUBAPI", url="https://api.github.com", active=True, method="GET", expected_status=200, interval_value= 20)
    #session.add(monitor_1)
    #session.commit()
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
              "active":monitor.active,
              "method":monitor.method,
              "expected_status":monitor.expected_status,
              "interval_value":monitor.interval_value
            }
          r.hset(key, mapping=maps)
    
          monitoring_result = httpEngine(mon)
          session.add(monitoring_result)
          session.commit()
          result_monitoring = session.execute(statement=stmt_res)
    
    

         
           
