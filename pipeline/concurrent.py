import asyncio

from pipeline.worker import process_record
async def concurrent_pipeline(records):
    tasks = [
        asyncio.create_task(
            process_record(record, retries=3, timeout=2)
        )
        for record in records
    ]

    try:
        results = await asyncio.gather(*tasks)

    except asyncio.CancelledError:
        # Gracefully cancel all running tasks
        for task in tasks:
            if not task.done():
                task.cancel()

        # Wait for all tasks to finish cancellation
        await asyncio.gather(*tasks, return_exceptions=True)

        raise

    return [
        result
        for result in results
        if result is not None
    ]