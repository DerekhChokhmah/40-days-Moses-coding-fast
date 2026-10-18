import httpx
import time 
from app.models import MonitoringResult
from app.metrics import prometheus_collector, counter
def httpEngine(result):
      link = result.url
      s_code = result.expected_status
      start_time = time.perf_counter()
      try:
        response = httpx.get(link)
        end_time = time.perf_counter() 
        diff = end_time - start_time
        prometheus_collector(diff)
        if s_code == response.status_code:
          success_status = True
          counter.labels(outcome="success").inc()
        else:
          success_status = False
          counter.labels(outcome="failure").inc()
        monitor_result = MonitoringResult(monitor_id=result.id, status_code=response.status_code, success=success_status,response_time=diff)
        return monitor_result
      except httpx.TimeoutException:
        print("Timeout error endpoint check failed")
        end_time = time.perf_counter()
        diff = end_time - start_time
        prometheus_collector(diff) 
        counter.labels(outcome="timeout").inc()
        monitor_result = MonitoringResult(monitor_id=result.id, status_code=None, success=False, response_time=diff)
        return monitor_result  
      except httpx.ConnectError:
        print("Connection Error")
        end_time = time.perf_counter()
        diff = end_time - start_time
        prometheus_collector(diff) 
        counter.labels(outcome="connection_error").inc()
        monitor_result = MonitoringResult(monitor_id=result.id, status_code=None, success=False, response_time=diff)
        return monitor_result
      except:
        print("Error")  
        end_time = time.perf_counter() 
        diff = end_time - start_time
        prometheus_collector(diff) 
        counter.labels(outcome="error").inc()
        monitor_result = MonitoringResult(monitor_id=result.id, status_code=None, success=False, response_time=diff)
        return monitor_result 
        
      

      