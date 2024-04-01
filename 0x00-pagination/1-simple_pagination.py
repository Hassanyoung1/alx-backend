#!/usr/bin/env python3

"""
This module contains a single function index_range thati
takes two integers
"""

from typing import List, Tuple
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """
    a function named index_range that takes two integer
    """
    return (page - 1) * page_size,  (((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve the requested page from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of records per page (default is 10).

        Returns:
             List[List]: The dataset page corresponding to the requested page.
        """

        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        index = index_range(page, page_size)
        data = self.dataset()
        if index[0] > len(data):
            return []
        return data[index[0]:index[1]]
