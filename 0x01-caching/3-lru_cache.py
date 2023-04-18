#!/usr/bin/env python3
"""LRU Caching policy

"""
from base_caching import BaseCaching
from datetime import datetime


class LRUCache(BaseCaching):
    """LRUCache class

    """

    def __init__(self):
        """Initializes the class

        """
        super().__init__()
        self.cache_keys = {}

    def put(self, key, item):
        """Puts an item in the cache

        Args:
            key (Any): Key to be stored in.
            item (Any): Item to be stored.
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_keys[key] = datetime.now()
            if len(self.cache_keys) > BaseCaching.MAX_ITEMS:
                lru_sort = sorted(self.cache_keys.items(), key=lambda x: x[1])
                lru_value = lru_sort[0]
                popped_key = lru_value[0]
                del self.cache_keys[popped_key]
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
            self.cache_keys[key] = datetime.now()
            return self.cache_data.get(key)
        return None
