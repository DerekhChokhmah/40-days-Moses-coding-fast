from sqlalchemy import create_engine, select, exc, text
from sqlalchemy.orm import sessionmaker
from models import Base, Monitor, MonitoringResult
from http_monitor import httpEngine
import os 
postgresql_db_password = os.environ["postgresql_db_password"]
                        #address of the db
engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql 
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
'''with Session() as session:
    session.add()
    session.commit() '''
stmt = select(Monitor).where(Monitor.id == 5)
stmt_res = select(MonitoringResult)
with Session() as session:
    '''monitor_1 = Monitor(id=1, name="GITHUBAPI", url="https://api.github.com", active=True, method="GET", expected_status=200, interval_value= 20)
    session.add(monitor_1)
    session.commit()'''
    result = session.execute(statement=stmt)
    monitoring_result = httpEngine(result)
    session.add(monitoring_result)
    session.commit()
    result_monitoring = session.execute(statement=stmt_res)
    for obj in result_monitoring.scalars():
        print(f"{obj.monitor_id}, {obj.response_time}, {obj.checked_at}, {obj.status_code}, {obj.success}")
    
