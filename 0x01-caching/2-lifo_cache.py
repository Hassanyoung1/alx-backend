#!/usr/bin/env python3

"""
Defines a LIFO (Last In, First Out) cache replacement policy.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO (Last In, First Out) caching strategy implementation.
    """

    def put(self, key, item):
        """
        Add an item to the cache using the LIFO replacement policy.

        Args:
            key: Key to access the item.
            item: Item to be stored in the cache.

        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print("DISCARD:", last_key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache if present.

        Args:
            key: Key to access the item.

        Returns:
            The item if found, None otherwise.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
