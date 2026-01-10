#!/usr/bin/env python3
"""
Measure the average runtime of the wait_n coroutine.
"""

import asyncio
import time
from typing import Union
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay)
    and return average time per coroutine.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    total_time: float = end_time - start_time

    return total_time / n
