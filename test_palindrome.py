# test_palindrome_partitioning.py
from typing import List, Tuple
import pytest

# --- tests -----------------------------------------------------------------

@pytest.fixture(params=[
    # LeetCode 131 - Example 1
    ("aab", [["a", "a", "b"], ["aa", "b"]]),
])
def case(request) -> Tuple[str, List[List[str]]]:
    """Fixture providing (input, expected) pairs."""
    return request.param

def _normalize_partitions(parts: List[List[str]]) -> List[tuple]:
    """Convert list-of-lists to a sorted list of tuples for order-insensitive comparison."""
    return sorted(tuple(p) for p in parts)

def test_partition(case):
    s, expected = case
    sol = Solution()
    result = sol.partition(s)
    assert _normalize_partitions(result) == _normalize_partitions(expected)


# --- main (runs the first example when executed as a script) ----------------

def main() -> None:
    """Run the first example and print the result (used when executed as a script)."""
    s = "aab"
    print("Input:", s)
    sol = Solution()
    try:
        out = sol.partition(s)
        print("Output:", out)
    except NotImplementedError:
        print("partition() is not implemented.")


# --- solution (left unimplemented as requested) -----------------------------

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Return all palindrome partitions of s.
        (Intentionally unimplemented for the testing task.)
        """
        res,par =[],[]

        def dfs(j,i):
            if i >= len(s):
                if i == j:
                    


if __name__ == "__main__":
    main()

