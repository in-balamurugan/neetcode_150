import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input, expected)
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
])
def case(request) -> Tuple[List[int], int]:
    """Fixture yielding (prices, expected) pairs."""
    return request.param


def test_max_profit_with_cooldown(case):
    prices, expected = case
    sol = Solution()
    assert sol.maxProfit(prices) == expected

from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Return the maximum profit with cooldown after selling.

        This method is intentionally left unimplemented for the user to fill in.
        """
        @lru_cache(None)
        def dfs(i, buying):
            if i >= len(prices):
                return 0

            cooldown = dfs (i+1,buying)
            
            if buying:

                buy = dfs(i+1, False) - prices[i]
                return max(buy,cooldown)
            else:
                sell = dfs(i+2, True) + prices[i]
                return max(sell,cooldown)


        return dfs(0,True)
