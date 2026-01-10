#!/usr/bin/env python3
"""
Run multiple task_wait_random coroutines concurrently
and return list of delays in order of completion.
"""
import asyncio
from typing import List
task_wait_random = import('3-tasks').task_wait_random
async def task_wait_n(n: int, max_delay: int) -> List[float]:
"""
Spawn task_wait_random n times with max_delay.
Return list of delays in order of completion without using sort().
"""
tasks = [task_wait_random(max_delay) for _ in range(n)]
delays: List[float] = []
for coro in asyncio.as_completed(tasks):
result: float = await coro
delays.append(result)
return delays
