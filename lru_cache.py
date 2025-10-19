import pytest


@pytest.fixture(params=[
    # Only the provided example test case (no extras)
    (
        ["LRUCache", "put", "get", "put", "put", "get", "get"],
        [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]],
        [None, None, 10, None, None, 20, -1],
    ),
])
def example_case(request):
    """
    Fixture yielding a single tuple:
      (operations_list, arguments_list, expected_output_list)
    """
    return request.param


def test_lru_cache(example_case):
    """
    Single test that runs the operations against the LRUCache class and compares to expected.
    """
    ops, args, expected = example_case

    outputs = []
    cache = None

    for op, arg in zip(ops, args):
        if op == "LRUCache":
            cache = LRUCache(arg[0])
            outputs.append(None)
        elif op == "put":
            cache.put(*arg)
            outputs.append(None)
        elif op == "get":
            outputs.append(cache.get(*arg))
        else:
            raise ValueError(f"Unknown operation: {op}")

    assert outputs == expected


def main():
    """
    Run the first example manually.
    """
    ops = ["LRUCache", "put", "get", "put", "put", "get", "get"]
    args = [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]]
    print("Example operations:", ops)
    print("Example arguments:", args)

    outputs = []
    cache = None
    try:
        for op, arg in zip(ops, args):
            if op == "LRUCache":
                cache = LRUCache(arg[0])
                outputs.append(None)
            elif op == "put":
                cache.put(*arg)
                outputs.append(None)
            elif op == "get":
                outputs.append(cache.get(*arg))
            else:
                raise ValueError(f"Unknown operation: {op}")
        print("Output:", outputs)
    except NotImplementedError:
        print("LRUCache methods are not implemented yet.")
    except Exception as e:
        print(f"An error occurred while running the example: {e}")


class LRUCache:
    """
    LRUCache class definition with unimplemented methods.
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with the given capacity.

        """
        from collections import OrderedDict
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Return the value corresponding to the key if it exists, otherwise -1.
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        Update or insert the value for the given key.
        If capacity exceeded, remove the least recently used item.
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    main()






