# test_decode_ways.py
import pytest

class Solution:
    """Solution container for the Decode Ways problem.

    Implement `numDecodings(self, s: str) -> int` to make the tests pass.
    """
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        for i in range(len(s) -1 ,-1,-1):
            print('\n',i,'\t',dp)
            if s[i] == "0":
                dp[i]=0
            else:
                dp[i]=dp[i+1]

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                dp[i] += dp[i + 2]
            print('\n',i,'\t',dp)
        return dp[0]

#def test_example_1():
#    sol = Solution()
#    assert sol.numDecodings("12") == 2


def test_example_2():
    sol = Solution()
    assert sol.numDecodings("1234512345") == 3

