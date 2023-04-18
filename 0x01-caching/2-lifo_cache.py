#!/usr/bin/env python3
"""Module containing LIFO Cache

"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class

    """

    def __init__(self):
        """Initializes the class

        """
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """Puts an item in the cache

        Args:
            key (Any): Key to be stored in.
            item (Any): Item to be stored.
        """
        if key and item:
            self.cache_data[key] = item
            if key in self.cache_keys:
                self.cache_keys.remove(key)
            self.cache_keys.append(key)
            if len(self.cache_keys) > BaseCaching.MAX_ITEMS:
                popped_key = self.cache_keys.pop(-2)
                del self.cache_data[popped_key]
                print("DISCARD: {}".format(popped_key))

    def get(self, key):
        """Gets item associated with a key

        Args:
            key (Any): Key to be searched for.

        Returns:
            Any: Item associated with a key.
        """
        if key and key in self.cache_data:
            return self.cache_data.get(key)
        return None
