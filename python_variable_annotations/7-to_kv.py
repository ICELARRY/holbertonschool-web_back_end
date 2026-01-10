#!/usr/bin/env python3
"""Type-annotated to_kv function"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is k and the second
    element is the square of v as a float
    """
    return (k, float(v ** 2))
