import asyncio


async def process_record(record, retries=3, timeout=2):
    """
    Process one record with timeout and retry handling.

    Returns the processed value when successful.
    Returns None when all retry attempts fail.
    """

    async def work():
        # Stage 1: Read
        value = record.strip()

        # Stage 2: Transform
        value = value.upper()

        # Stage 3: Validate
        if not value:
            return None

        # Stage 4: Simulate I/O-bound work
        await asyncio.sleep(0.1)

        return value

    for attempt in range(1, retries + 1):
        try:
            return await asyncio.wait_for(
                work(),
                timeout=timeout
            )

        except asyncio.TimeoutError:
            print(
                f"Timeout for '{record}' - "
                f"attempt {attempt}/{retries}"
            )

        except Exception as error:
            print(
                f"Error processing '{record}' - "
                f"attempt {attempt}/{retries}: {error}"
            )

    print(f"Failed after {retries} attempts: '{record}'")
    return None