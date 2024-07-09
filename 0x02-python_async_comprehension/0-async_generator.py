#!/usr/bin/env python3
"""Async Generator"""
from random import uniform
from asyncio import sleep
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float]:
    """Async Generator"""
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
