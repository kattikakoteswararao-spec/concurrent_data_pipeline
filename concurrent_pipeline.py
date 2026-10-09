import asyncio
import time


async def process_record(record, retries=3, timeout=2):
    """Process one record with retry and timeout handling."""

    for attempt in range(retries):
        try:
            async def work():
                # Stage 1: Read
                value = record.strip()

                # Stage 2: Transform
                value = value.upper()

                # Stage 3: Validate
                if not value:
                    return None

                # Stage 4: Simulate I/O work
                await asyncio.sleep(0.1)

                return value

            return await asyncio.wait_for(work(), timeout=timeout)

        except asyncio.TimeoutError:
            print(f"Timeout for '{record}' - attempt {attempt + 1}")

        except Exception as e:
            print(f"Error processing '{record}': {e}")

    print(f"Failed after {retries} attempts: '{record}'")
    return None


async def concurrent_pipeline(records):
    tasks = [
        process_record(record, retries=3, timeout=2)
        for record in records
    ]

    results = await asyncio.gather(*tasks)

    return [
        result for result in results
        if result is not None
    ]


async def main():

    records = [
        "user one",
        "user two",
        "user three",
        "user four",
        "user five",
    ]

    start_time = time.perf_counter()

    results = await concurrent_pipeline(records)

    end_time = time.perf_counter()

    print("Processed records:")

    for result in results:
        print(result)

    print()
    print(f"Total records: {len(results)}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())