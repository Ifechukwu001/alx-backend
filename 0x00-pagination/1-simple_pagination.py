#!/usr/bin/env python3
"""Module containing function that returns index range

"""
import csv
import math
from typing import List
import typing


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
        assert (type(page) == int and type(page_size) == int)
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset) or end >= len(dataset):
            return []
        return dataset[start:end]


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """Returns the index range corresponding to book size

    Args:
        page (int): Page number.
        page_size (int): Page size.

    Returns:
        typing.Tuple[int, int]: Tuple containing the list range
                                representing the page.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
