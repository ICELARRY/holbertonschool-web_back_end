#!/usr/bin/env python3
"""Type-annotated to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where first element is k and second is square of v as float"""
    return (k, float(v ** 2))
