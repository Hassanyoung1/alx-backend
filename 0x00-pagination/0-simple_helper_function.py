#!/usr/bin/env python3

"""
a function named index_range that takes two integer
arguments page and page_size and returns a tuple containing
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """
    a function named index_range that takes two integer
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
