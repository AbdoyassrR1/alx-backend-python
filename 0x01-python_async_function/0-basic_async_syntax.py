#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay=10):
    """return a float value between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
