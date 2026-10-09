import argparse
import asyncio

from pipeline.sequential import run_sequential
from pipeline.concurrent import concurrent_pipeline


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Concurrent Data Processing Pipeline"
    )

    parser.add_argument(
        "--mode",
        choices=["sequential", "concurrent"],
        default="concurrent",
        help="Pipeline execution mode"
    )

    parser.add_argument(
        "--records",
        nargs="+",
        default=[
            "user one",
            "user two",
            "user three",
            "user four",
            "user five",
        ],
        help="Records to process"
    )

    return parser.parse_args()


async def run_concurrent(records):
    return await concurrent_pipeline(records)


async def main():
    args = parse_arguments()

    records = args.records

    print(f"Running {args.mode} pipeline...")
    print()

    if args.mode == "sequential":
        results, execution_time = run_sequential(records)

    else:
        start_results = asyncio.get_running_loop().time()

        results = await run_concurrent(records)

        end_results = asyncio.get_running_loop().time()
        execution_time = end_results - start_results

    print("Processed records:")

    for result in results:
        print(result)

    print()
    print(f"Total records: {len(results)}")
    print(f"Execution time: {execution_time:.4f} seconds")


if __name__ == "__main__":
    asyncio.run(main())