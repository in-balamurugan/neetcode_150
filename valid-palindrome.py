# palindrome_test.py
import pytest
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Implement this function.

        A phrase is a palindrome if, after converting all uppercase letters into
        lowercase letters and removing all non-alphanumeric characters, it reads
        the same forward and backward.
        """
        s=re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return s == s[::-1]

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),  # Example 1
        ("race a car", False),                     # Example 2
        (" ", True),                               # Example 3
    ],
)
def test_is_palindrome(solver, s, expected):
    assert solver.isPalindrome(s) == expected


# Allow running directly: python palindrome_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

