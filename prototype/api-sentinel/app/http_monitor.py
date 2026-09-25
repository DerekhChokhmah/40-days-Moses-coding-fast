import httpx
import time 
def httpEngine(result):
    for rec in result.scalars():
      link = rec.url
      start_time = time.perf_counter()
      response = httpx.get(link)
      end_time = time.perf_counter()
      diff = end_time - start_time
      print(diff)
      print(response)

      