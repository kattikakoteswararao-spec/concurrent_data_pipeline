import time


def process_record(record):
    """
    Process one record sequentially.

    Stages:
    1. Read
    2. Transform
    3. Validate
    4. Simulate I/O work
    """

    # Stage 1: Read
    value = record.strip()

    # Stage 2: Transform
    value = value.upper()

    # Stage 3: Validate
    if not value:
        return None

    # Stage 4: Simulate I/O-bound work
    time.sleep(0.1)

    return value


def sequential_pipeline(records):
    """
    Process all records sequentially.
    """

    results = []

    for record in records:
        result = process_record(record)

        if result is not None:
            results.append(result)

    return results


def run_sequential(records):
    """
    Run the sequential pipeline and measure execution time.
    """

    start_time = time.perf_counter()

    results = sequential_pipeline(records)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return results, execution_time