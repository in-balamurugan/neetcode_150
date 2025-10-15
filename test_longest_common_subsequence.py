import pytest
from typing import Tuple


@pytest.fixture(params=[
    # (input (text1, text2), expected)
    (("abcde", "ace"), 3),
    (("abc", "abc"), 3),
    (("abc", "def"), 0),
])
def case(request) -> Tuple[Tuple[str, str], int]:
    """Fixture yielding ((text1, text2), expected) pairs."""
    return request.param


def test_longest_common_subsequence(case):
    (text1, text2), expected = case
    sol = Solution()
    assert sol.longestCommonSubsequence(text1, text2) == expected


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence between text1 and text2.
        This method is intentionally left unimplemented for the user to fill in.
        """
        
        lt1 =len(text1)
        lt2=len(text2)
        dp = [[ 0 for _ in range(lt2 +1)]
                  for  _ in range(lt1 +1) ]

        for i in range(lt1-1,-1,-1):

            for j in range(lt2-1,-1,-1):


                if text1[i] == text2[j]:

                    dp[i][j] = 1 + dp[i+1][j+1] 

                else:

                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

