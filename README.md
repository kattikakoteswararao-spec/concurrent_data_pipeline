# Concurrent Data Processing Pipeline

## Overview

This project implements a reusable data processing pipeline using Python.

The pipeline processes records through multiple stages:

1. Read
2. Transform
3. Validate
4. Simulate I/O processing

The project contains both a sequential implementation and an asynchronous concurrent implementation. The performance of both approaches is measured and compared.

## Project Structure

concurrent_data_pipeline/
│
├── pipeline/
│   ├── __init__.py
│   ├── sequential.py
│   ├── concurrent.py
│   └── worker.py
│
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py
│
├── benchmark.py
├── main.py
├── README.md
└── requirements.txt

## Requirements

Python 3.10+
pytest

## Setup

Create and activate a virtual environment:

bashpython -m venv venv

Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Running the Application:

Sequential Processing
python main.py --mode sequential

Concurrent Processing
python main.py --mode concurrent

Running Tests

Run all tests using:
pytest

Expected result:
3 passed

Performance Benchmark
Run:
python benchmark.py
The benchmark compares sequential and concurrent execution.

Example result:
Sequential time : 0.5026 seconds
Concurrent time : 0.1156 seconds
Speedup          : 4.35x
Results match    : True

The concurrent implementation processes the records significantly faster while producing the same results.

## Profiling

The application can also be profiled using Python’s cProfile:
python -m cProfile -s cumulative benchmark.py

This helps identify which functions consume the most execution time.


## Performance Bottleneck and Improvement

The main bottleneck in the sequential implementation is the simulated
I/O-bound operation (asyncio.sleep(0.1)) performed for each record.

In the sequential implementation, each record waits for the I/O operation
to complete before the next record is processed.

The concurrent implementation uses asyncio to process multiple records
at the same time. This allows the I/O wait time to overlap and improves
overall execution time.

The benchmark showed a speedup of approximately 3.73x while producing
the same results.

## Features
Concurrent/asynchronous processing
Multiple processing stages
Input validation
Empty-record handling
Automated unit tests
Performance benchmarking
cProfile-based performance analysis
