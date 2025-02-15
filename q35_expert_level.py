"""Question: Define a class Cache with a private class attribute _cache
to store cached values. Use class methods to add, retrieve, and clear cache entries.
"""


# Iris solution
class Cache:
    _cache = {}

    @classmethod
    def add(cls, key, value):
        cls._cache[key] = value

    @classmethod
    def get(cls, key):
        return cls._cache.get(key, None)

    @classmethod
    def clear(cls):
        cls._cache.clear()

# Use class methods to manipulate cache
Cache.add("key1", "value1")
print(Cache.get("key1"))  # Output: value1
Cache.clear()
print(Cache.get("key1"))  # Output: None
