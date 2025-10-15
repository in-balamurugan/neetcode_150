# min_window_test.py
import pytest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Implement this function.

        Given strings s and t, return the minimum window in s which will contain all
        the characters in t (including duplicates). If no such window exists, return "".

        The testcases guarantee the answer is unique.
        """
        raise NotImplementedError("Implement this method in the Solution class")


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),  # Example 1
        ("a", "a", "a"),                   # Example 2
        ("a", "aa", ""),                   # Example 3
    ],
)
def test_min_window_examples(solver, s, t, expected):
    assert solver.minWindow(s, t) == expected

# Allow running directly: python min_window_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

