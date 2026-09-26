import httpx
import time 
from models import MonitoringResult

def httpEngine(result):
    for rec in result.scalars():
      link = rec.url
      s_code = rec.expected_status
      start_time = time.perf_counter()
      try:
        response = httpx.get(link)
        end_time = time.perf_counter()
        diff = end_time - start_time
        if s_code == response.status_code:
          success_status = True
        else:
          success_status = False
        monitor_result = MonitoringResult(monitor_id=rec.id, status_code=response.status_code, success=success_status,response_time=diff)
        return monitor_result
      except httpx.TimeoutException:
        print("Timeout error endpoint check failed")
        end_time = time.perf_counter()
        diff = end_time - start_time
        monitor_result = MonitoringResult(monitor_id=rec.id, status_code=None, success=False, response_time=diff)
        return monitor_result  
      except httpx.ConnectError:
        print("Connection Error")
        end_time = time.perf_counter()
        diff = end_time - start_time
        monitor_result = MonitoringResult(monitor_id=rec.id, status_code=None, success=False, response_time=diff)
        return monitor_result
      except:
        print("Error")  
        end_time = time.perf_counter()
        diff = end_time - start_time
        monitor_result = MonitoringResult(monitor_id=rec.id, status_code=None, success=False, response_time=diff)
        return monitor_result  
        
      

      