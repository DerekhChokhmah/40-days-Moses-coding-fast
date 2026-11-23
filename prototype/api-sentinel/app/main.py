from fastapi import FastAPI, Depends
from sqlalchemy import select
from app.schemas import schemaForMonitorAPI
from app.database import Session, exc, text
#from sqlalchemy import select
from app.models import Monitor, MonitoringResult
from app.security import verify_api_key
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
Instrumentator.instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False
)

@app.post("/monitors", dependencies=[Depends(verify_api_key)])
async def create_monitor_data(schema: schemaForMonitorAPI):
    
    with Session() as session:
        #stmt = select(Monitor)
        monitor_2 = Monitor(name= schema.name, active=schema.active, url=schema.url, method=schema.method, expected_status=schema.expected_status, interval_value=schema.interval_value)
        session.add(monitor_2)
        session.commit()
        return "OK"
@app.get("/get-monitors", dependencies=[Depends(verify_api_key)])
async def get_monitor_data():
    stmt = select(Monitor)
    with Session() as session:
        result = session.execute(stmt)
        return result.scalars().all()
@app.get("/get-monitoring-results", dependencies=[Depends(verify_api_key)])
async def get_monitoring_results():
    stmt_res = select(MonitoringResult)
    with Session() as session:
        result_monitoring = session.execute(stmt_res)
        return result_monitoring.scalars().all()    
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
     
   
       
