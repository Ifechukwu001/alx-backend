#!/usr/bin/env python3
"""Module class for a basic dictionary.

"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class

    """

    def put(self, key, item):
        """Puts an item in the cache

        Args:
            key (Any): Key to store the data.
            item (Any): Item to be stored.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets item at a key

        Args:
            key (Any): Key to search.

        Returns:
            Any: The item stored at a key.
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
