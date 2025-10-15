# max_profit_test.py
import pytest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Implement this function.

        You are given an array prices where prices[i] is the price of a stock on day i.
        You want to maximize your profit by choosing one day to buy and a different future
        day to sell. Return the maximum profit achievable. If no profit is possible, return 0.
        """
        profit=0
        lowest_price =prices[0]
        i=0
        p_len = len(prices)

        while i < p_len:
            curr_price = prices[i]
            lowest_price = min(prices[i], lowest_price)
            profit=max(profit,curr_price-lowest_price)
            i +=  1


        return profit

        


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7,1,5,3,6,4], 5),  # Example 1
        ([7,6,4,3,1], 0),    # Example 2
    ],
)
def test_max_profit_examples(solver, prices, expected):
    assert solver.maxProfit(prices) == expected


# Allow running directly: python max_profit_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

