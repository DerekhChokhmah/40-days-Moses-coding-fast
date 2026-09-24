import httpx
response = httpx.get("https://httpbin.org/delay/10")
print(response)