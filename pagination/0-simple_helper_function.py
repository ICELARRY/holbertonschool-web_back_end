#!/usr/bin/env python3
"""
Simple helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple containing the start index and end index
    for pagination parameters.

    Page numbers are 1-indexed.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
