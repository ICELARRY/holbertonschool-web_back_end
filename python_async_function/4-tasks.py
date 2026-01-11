#!/usr/bin/env python3
"""
Run multiple task_wait_random coroutines concurrently
and return the list of delays sorted in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay.
    Return the list of delays sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    delays.sort()
    return delays
