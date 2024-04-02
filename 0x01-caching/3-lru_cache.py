#!/usr/bin/env python3
"""

"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def put(self, key, item):
        """
        Adds an item to the cache.
        Args:
            key: The key for the item to add.
            item: The item to add to the cache.
        Returns:
            None
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_discarded = next(iter(self.cache_data))
            del self.cache_data[key_discarded]
            print("DISCARD: {}".format(key_discarded))
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item associated with the given key from the cache.

        Args:
            key: The key to retrieve the item for.

        Returns:
            The item associated with the key, or None if the key
            does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value

        return value
