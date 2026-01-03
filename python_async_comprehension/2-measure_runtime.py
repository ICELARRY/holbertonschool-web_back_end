#!/usr/bin/env python3
"""
Measure runtime for four parallel async comprehensions
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure total runtime for running async_comprehension 4 times in parallel
    """
    start = time.perf_counter()
    # Create a list of coroutines
    coroutines = [async_comprehension() for _ in range(4)]
    # Run all coroutines concurrently using gather with *args
    await asyncio.gather(*coroutines)
    end = time.perf_counter()
    return end - start
