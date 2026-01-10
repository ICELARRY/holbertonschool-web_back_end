#!/usr/bin/env python3
"""Test for async coroutines"""

import asyncio
from basic_async_syntax import wait_random
from concurrent_coroutines import wait_n

# Run wait_random with default max_delay=10
print(asyncio.run(wait_random()))
# Run wait_random with max_delay=5
print(asyncio.run(wait_random(5)))
# Run wait_random with max_delay=15
print(asyncio.run(wait_random(15)))

# Test wait_n
print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
