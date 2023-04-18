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
        """Gets a dataset representing the page

        Args:
            page(int): Page number.
            page_size (int): Page size.

        Returns:
            List[List]: Dataset.
        """
        assert (type(page) == int and type(page_size) == int)
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        elif end >= len(dataset):
            return dataset[start:len(dataset)]
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> typing.Dict:
        """Gets a more sophiticated data information about the page.

        Args:
            page (int): Page number
            page_size (int): Page size.

        Returns:
            Dict: Dictionary of the page information.
        """
        pagee = self.get_page(page, page_size)
        full_data = self.__dataset
        total_pages = math.ceil(len(full_data) / page_size)
        next = page + 1 if page + 1 <= total_pages else None
        prev = page - 1 if page - 1 else None
        return {
            "page_size": len(pagee),
            "page": page,
            "data": pagee,
            "next_page": next,
            "prev_page": prev,
            "total_pages": total_pages,
        }


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
