# test_palindromic_substrings.py
import pytest
from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Given a string s, return the number of substrings within s that are palindromes.

        Constraints:
          1 <= s.length <= 1000
          s consists of lowercase English letters.
        """

        n =len(s)
        index=0
        length=0
        count=0
        dp = [[False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):

                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    count += 1

        return count
                    
        

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected",
    [
        # Example 1
        ("abc", 3),   # "a", "b", "c"
        # Example 2
        ("aaa", 6),   # "a","a","a","aa","aa","aaa"

        # Small / edge cases
        ("a", 1),     # single char
        ("aa", 3),    # "a","a","aa"
        ("ab", 2),    # "a","b"

        # Mixed cases
        ("aba", 4),   # "a","b","a","aba"
        ("abba", 6),  # "a","b","b","a","bb","abba"
        
        # Larger but deterministic small example
        ("racecar", 10),  # common test (palindromes include single chars 7, plus others like "cec","aceca","racecar","cec"?)
    ],
)
def test_count_substrings(solver, s, expected):
    assert solver.countSubstrings(s) == expected


# Allow running directly: python test_palindromic_substrings.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

