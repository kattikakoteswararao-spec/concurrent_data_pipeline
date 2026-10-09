import time
import asyncio
import cProfile
import pstats
import psutil

from pipeline.sequential import sequential_pipeline
from pipeline.concurrent import concurrent_pipeline


records = [
    "user one",
    "user two",
    "user three",
    "user four",
    "user five",
]


# Sequential benchmark
start = time.perf_counter()

sequential_results = sequential_pipeline(records)

sequential_time = time.perf_counter() - start


# Concurrent benchmark
async def run_concurrent():
    start = time.perf_counter()

    results = await concurrent_pipeline(records)

    concurrent_time = time.perf_counter() - start

    return results, concurrent_time


concurrent_results, concurrent_time = asyncio.run(run_concurrent())


# Performance metrics
total_records = len(records)

throughput = total_records / concurrent_time if concurrent_time > 0 else 0
average_latency = concurrent_time / total_records if total_records > 0 else 0

process = psutil.Process()

cpu_usage = process.cpu_percent(interval=0.1)
memory_usage = process.memory_info().rss / (1024 * 1024)

print()
print("=== PERFORMANCE METRICS ===")
print(f"Total records       : {total_records}")
print(f"Throughput          : {throughput:.2f} records/second")
print(f"Average latency     : {average_latency:.4f} seconds/record")
print(f"CPU usage           : {cpu_usage:.2f}%")
print(f"Memory usage        : {memory_usage:.2f} MB")

# Performance comparison
print()
print("==== PERFORMANCE COMPARISON ====")
print()

print(f"Sequential time : {sequential_time:.4f} seconds")
print(f"Concurrent time : {concurrent_time:.4f} seconds")

speedup = sequential_time / concurrent_time

print(f"Speedup         : {speedup:.2f}x")

print()
print(f"Results match: {sequential_results == concurrent_results}")

print()
print("=== PROFILING CONCURRENT PIPELINE ===")

profiler = cProfile.Profile()

profiler.enable()
asyncio.run(concurrent_pipeline(records))
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("cumulative")
stats.print_stats(10)

