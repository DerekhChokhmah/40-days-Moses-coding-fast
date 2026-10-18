from fastapi import FastAPI
from app.schemas import schemaForMonitorAPI
from app.database import Session, exc, text
#from sqlalchemy import select
from app.models import Monitor

app = FastAPI()


@app.post("/monitors")
async def create_monitor_data(schema: schemaForMonitorAPI):
    
    with Session() as session:
        #stmt = select(Monitor)
        monitor_2 = Monitor(name= schema.name, active=schema.active, url=schema.url, method=schema.method, expected_status=schema.expected_status, interval_value=schema.interval_value)
        session.add(monitor_2)
        session.commit()
        return "OK"

@app.get("/health")
async def check_health():
   health = {}
   health["FASTAPI status"] = "OK"
   with Session() as session:
          try:
            session.execute(text("SELECT 1"))
            health["PostgreSQL status"] = "OK"
          except exc.DBAPIError:
              health["PostgreSQL status"] = "UNHEALTHY"  
       
   return health 
     
   
       
