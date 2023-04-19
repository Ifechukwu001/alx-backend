#!/usr/bin/env python3
"""LFU Caching policy

"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class

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
            if len(self.cache_keys) == BaseCaching.MAX_ITEMS:
                lfu_sort = sorted(self.cache_keys.items(), key=lambda x: x[1])
                lfu_value = lfu_sort[0]
                popped_key = lfu_value[0]
                del self.cache_data[popped_key]
                if popped_key == key:
                    pass
                else:
                    del self.cache_keys[popped_key]
                    print("DISCARD: {}".format(popped_key))
            self.cache_data[key] = item
            if key in self.cache_keys:
                self.cache_keys[key] = self.cache_keys[key] + 1
            else:
                self.cache_keys[key] = 0

    def get(self, key):
        """Gets item associated with a key

        Args:
            key (Any): Key to be searched for.

        Returns:
            Any: Item associated with a key.
        """
        if key and key in self.cache_data:
            self.cache_keys[key] = self.cache_keys[key] + 1
            return self.cache_data.get(key)
        return None
