#!/usr/bin/env python3
"""Hypermedia pagination"""

import math
from simple_pagination import Server as BaseServer, index_range


class Server(BaseServer):
    """Server class with hypermedia pagination"""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return dictionary with hypermedia pagination info"""
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
