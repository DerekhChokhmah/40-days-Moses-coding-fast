from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import Base, Monitor, MonitoringResult
import os 
postgresql_db_password = os.environ["postgresql_db_password"]
                        #address of the db
engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql 
Session = sessionmaker(engine)
'''with Session() as session:
    session.add()
    session.commit() '''
stmt = select(Monitor).where(Monitor.id == 1)
with Session() as session:
    #monitor_1 = Monitor(id=1, name="GITHUBAPI", url="https://api.github.com", active=True)
    #session.add(monitor_1)
    #session.commit()
    result = session.execute(statement=stmt)
    for obj in result.scalars():
        print(f"{obj.id}, {obj.url}, {obj.active}")
    
Base.metadata.create_all(engine)