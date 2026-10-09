from pipeline.sequential import sequential_pipeline
from pipeline.concurrent import concurrent_pipeline


def test_sequential_pipeline():
    records = [
        "user one",
        "user two",
        "user three",
    ]

    results = sequential_pipeline(records)

    assert results == [
        "USER ONE",
        "USER TWO",
        "USER THREE",
    ]


def test_concurrent_pipeline():
    records = [
        "user one",
        "user two",
        "user three",
    ]

    import asyncio

    results = asyncio.run(
        concurrent_pipeline(records)
    )

    assert results == [
        "USER ONE",
        "USER TWO",
        "USER THREE",
    ]


def test_empty_record():
    records = [
        "user one",
        "",
        "user three",
    ]

    import asyncio

    results = asyncio.run(
        concurrent_pipeline(records)
    )

    assert results == [
        "USER ONE",
        "USER THREE",
    ]