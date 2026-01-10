#!/usr/bin/env python3
"""
Run multiple task_wait_random coroutines concurrently
and return list of delays in order of completion.
"""

import asyncio
from typing import List

# doğru import
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay.
    Return list of delays in ascending order without using sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    # asyncio.as_completed yields tasks as they finish
    for coro in asyncio.as_completed(tasks):
        result: float = await coro
        delays.append(result)

    return delays
