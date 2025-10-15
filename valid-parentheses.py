# brackets_test.py
import pytest

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Implement this function.

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.
        """
        raise NotImplementedError("Implement this method in the Solution class")


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),        # Example 1
        ("()[]{}", True),    # Example 2
        ("(]", False),       # Example 3
        ("([])", True),      # Example 4
        ("([)]", False),     # Example 5
    ],
)
def test_is_valid(solver, s, expected):
    assert solver.isValid(s) == expected


# Allow running with: python brackets_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

