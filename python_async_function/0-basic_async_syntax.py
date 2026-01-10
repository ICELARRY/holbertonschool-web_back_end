#!/usr/bin/env python3
"""Asynchronous wait_random coroutine"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

