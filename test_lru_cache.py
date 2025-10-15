# test_lru_cache.py
import pytest

"""
PyTest file for the LRU Cache problem.

Requirements implemented in this file:
- A single Solution class is defined at the bottom.
- The target method (run_operations) exists but is unimplemented (raises NotImplementedError).
- Tests use a single pytest.fixture with params containing the provided (input, expected) pair(s).
- One test function uses that fixture to test the method.
- A main() function that runs the first example is included before the Solution class, and guarded
  so it only runs when the file is executed as a script.
"""

@pytest.fixture(params=[
    # Each entry is a tuple: (operations_list, arguments_list, expected_output_list)
    # Example provided in the prompt:
    (
        ["LRUCache", "put", "get", "put", "put", "get", "get"],
        [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]],
        [None, None, 10, None, None, 20, -1]  # 'null' in prompt translated to Python None
    ),
])
def example_case(request):
    return request.param

def test_run_operations(example_case):
    operations, arguments, expected = example_case
    sol = Solution()
    result = sol.run_operations(operations, arguments)
    assert result == expected

def main():
    """
    Run the first example from the problem statement and print the result.
    This function will be executed only when the module is run as a script.
    """
    operations = ["LRUCache", "put", "get", "put", "put", "get", "get"]
    arguments = [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]]
    print("Running example operations:")
    print(operations)
    print(arguments)
    sol = Solution()
    output = sol.run_operations(operations, arguments)
    print("Output:")
    print(output)

# Solution class must be defined at the bottom and the target method must be unimplemented.
class Solution:
    def run_operations(self, operations, arguments):
        """
        Run a sequence of LRU cache operations.

        Parameters
        ----------
        operations : List[str]
            e.g. ["LRUCache", "put", "get", ...]
        arguments : List[List[int]]
            e.g. [[2], [1,10], [1], ...]

        Returns
        -------
        List[Optional[int]]
            Results corresponding to each operation, where 'put' and 'LRUCache' return None,
            and 'get' returns either the value or -1.
        """
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    main()
