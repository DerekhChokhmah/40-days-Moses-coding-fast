from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os 
postgresql_db_password = os.environ["postgresql_db_password"]
                        #address of the db
engine = create_engine("postgresql+psycopg2://postgres:{}@localhost:8084/api_sentinel".format(postgresql_db_password))
         # does the connection between sqlalchemy and postgresql 
Session = sessionmaker(engine)
'''with Session() as session:
    session.add()
    session.commit() '''



