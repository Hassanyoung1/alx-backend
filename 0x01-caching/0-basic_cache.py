#!/usr/bin/env python3

"""
A class BasicCache that inherits from BaseCaching and is a caching system.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    A class BasicCache that inherits from BaseCaching and
    implements a basic       caching system.

    Methods:
        put(self, key, item): Inserts an item into the
        cache with the given key.
        get(self, key): Retrieves the item associated
        with the given key from the cache.

    Attributes:
        cache_data: A dictionary to store cached items.
    """

    def put(self, key, item):
        """
        Inserts an item into the cache with the given key.

        Args:
            key: The key to associate with the item.
            item: The item to be cached.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the item associated with the given key from the cache.

        Args:
            key: The key to retrieve the item for.

        Returns:
            The item associated with the key, or None
            if the key does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
