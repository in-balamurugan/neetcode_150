import pytest
from typing import Tuple


@pytest.fixture(params=[
    # (input, expected)
    ((3, 7), 28),
    ((3, 2), 3),
])
def case(request) -> Tuple[Tuple[int, int], int]:
    """Fixture yielding ((m, n), expected) pairs."""
    return request.param


def test_unique_paths(case):
    (m, n), expected = case
    sol = Solution()
    assert sol.uniquePaths(m, n) == expected


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """Return the number of unique paths from top-left to bottom-right.
        """

        #m rows , n columns
        dp=[ [0]* (n+1) for _ in range(m+1) ]

        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
            
                dp[i][j] += dp[i+1][j] + dp[i][j+1]

        print(dp)
        
        return dp[0][0] 
