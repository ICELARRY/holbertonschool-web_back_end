#!/usr/bin/env python3
"""Execute multiple coroutines concurrently and return delays in order of completion"""

import asyncio
from basic_async_syntax import wait_random
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay.
    Return list of delays in ascending order without using sort()
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for coro in asyncio.as_completed(tasks):
        result: float = await coro
        delays.append(result)

    return delays
