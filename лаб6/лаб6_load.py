import json
import time
import urllib.request

URL = "http://127.0.0.1:8080/"
REQUESTS = 50


def one_call():
    started = time.perf_counter()
    with urllib.request.urlopen(URL, timeout=2) as response:
        body = json.loads(response.read().decode())
    return (time.perf_counter() - started) * 1000, body


latencies = []
for _ in range(REQUESTS):
    elapsed, payload = one_call()
    latencies.append(elapsed)

latencies.sort()
p95 = latencies[max(0, int(len(latencies) * 0.95) - 1)]
print(f"запросов {REQUESTS}, последний served {payload.get('served')}, p95 {p95:.2f} мс")
