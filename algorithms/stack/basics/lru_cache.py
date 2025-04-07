from collections import OrderedDict
class LRUCache:
    """
    Implement a Least Recently Used (LRU) cache.

    LC. 146 LRU Cache
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.usage = OrderedDict()

    # Analysis: time = O(1)
    def get(self, key: int) -> int:
        if len(self.usage) == 0 or key not in self.usage:
            return -1
               
        self.usage.move_to_end(key)
        return self.usage[key]
        
    # Analysis: time = O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.usage:
            self.usage.move_to_end(key)
            self.usage[key] = value
        else:
            if len(self.usage) == self.capacity:
                self.usage.popitem(last=False)
            self.usage[key] = value


if __name__ == "__main__":
    cache = LRUCache(2)

    ops = [
        ("put", 1, 1),
        ("put", 2, 2),
        ("get", 1, 1),
        ("put", 3, 3),
        ("get", 2, -1),
        ("put", 4, 4),
        ("get", 1, -1),
        ("get", 3, 3),
        ("get", 4, 4)
    ]

    for i, op in enumerate(ops, 1):
        if op[0] == "put":
            _, key, val = op
            cache.put(key, val)
        elif op[0] == "get":
            _, key, expected = op
            output = cache.get(key)
            assert output == expected, f"Test case {i} failed: expected {expected}, got {output}"

    print("All test cases passed!")
