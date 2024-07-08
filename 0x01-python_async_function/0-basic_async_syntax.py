#!/usr/bin/env python3
"""The basics of async"""
from random import uniform


async def wait_random(max_delay=10):
    """return a float value between 0 and max_delay"""
    return uniform(0, max_delay)
