# test_longest_palindrome.py
import pytest
from typing import Tuple

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Return the longest palindromic substring of s.
        Approach: expand around each center (odd and even length palindromes).
        Time: O(n^2), Space: O(1) extra.
        """
        index,length =0,0
        n=len(s)

        dp = [ [False]*n for _ in range(n)]

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                print(i,j)
                
                if s[i] == s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    print('\t',i+1,j-1) if j-i>2 else '' 
                    if length < (j-i+1):
                        index=i
                        length=j-i+1
        return s[index:index+length]


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected_lengths",
    [
        # Provided examples (either answer is acceptable if same length)
        ("abcacba", {7}),    # "aba" or "bab" -> length 3
        #("abbc", {2}),     # "bb" -> length 2

    ],
)
def test_longest_palindrome_length(solver, s, expected_lengths):
    res = solver.longestPalindrome(s)
    assert len(res) in expected_lengths
    # result must be palindrome
    assert res == res[::-1]
    # result must be substring of original
    assert res in s





# Allow running directly: python test_longest_palindrome.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-s", __file__]))
    #Solution().longestPalindrome("abcbc")
