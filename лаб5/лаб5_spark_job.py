import json
import time

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

LIMIT_MS = 65

spark = SparkSession.builder.appName("lab5-reviews").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

reviews = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:9092")
    .option("subscribe", "reviews")
    .option("startingOffsets", "earliest")
    .load()
)


def score_batch(batch, _epoch):
    rows = batch.select(col("value").cast("string")).collect()
    latencies = []
    for row in rows:
        if not row[0]:
            continue
        started = time.perf_counter()
        payload = json.loads(row[0])
        _positive = int(float(payload.get("rating", 0)) >= 4)
        latencies.append((time.perf_counter() - started) * 1000)
    if not latencies:
        return
    latencies.sort()
    index = min(len(latencies) - 1, max(0, int(len(latencies) * 0.95) - 1))
    p95 = latencies[index]
    print(f"событий {len(latencies)}, p95 {p95:.3f} мс, порог {LIMIT_MS} мс, выполнен {p95 < LIMIT_MS}")


(
    reviews.writeStream.foreachBatch(score_batch)
    .option("checkpointLocation", "/tmp/lab5-reviews")
    .start()
    .awaitTermination()
)
