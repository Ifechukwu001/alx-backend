#!/usr/bin/env python3
"""Module containing function that returns index range

"""
import typing


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
