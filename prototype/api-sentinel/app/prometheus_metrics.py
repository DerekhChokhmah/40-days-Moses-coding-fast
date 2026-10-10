from prometheus_client import Histogram
def prometheus_collector(end_time, time_response):
    h = Histogram(end_time, "Response time for http monitoring result responses")
    h.observe(time_response)