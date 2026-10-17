from prometheus_client import Histogram, start_http_server, Counter
h = Histogram('http_response_duration_seconds', "Response time for http monitoring result responses", buckets=[0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5])
counter = Counter('http_monitor_checks_total', "Total HTTP monitoring checks by outcome", ["outcome"])   
def prometheus_collector(time_response):
    h.observe(time_response)

def start_prometheus_server():
    start_http_server(8000)
