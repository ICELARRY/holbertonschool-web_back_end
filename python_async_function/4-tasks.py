#!/usr/bin/env python3
"""
4-tasks.py
Create task_wait_n function using task_wait_random
"""

import asyncio
from typing import List

task_wait_random = _import_('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random multiple times

    Args:
        n: execution count
        max_delay: delay limit

    Returns:
        ordered delay values
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    all_values = await asyncio.gather(*tasks)

    ordered = []
    for val in all_values:
        pos = 0
        while pos < len(ordered) and val > ordered[pos]:
            pos += 1
        ordered.insert(pos, val)

    return ordered
