import pytest

class Solution:
    """
    Skeleton for the Coin Change problem.

    Implement `coinChange(self, coins: list[int], amount: int) -> int`:
    Given an integer array coins and an integer amount, return the fewest
    number of coins that you need to make up that amount. If that amount of
    money cannot be made up by any combination of the coins, return -1.
    """

    def coinChange(self, coins: list[int], amount: int) -> int:
        
        dp=[amount+1]*(amount+1)
        dp[0]=0

        print(f'For {amount}')
        for a in range(1,amount+1):
            for c in coins:
                if a>=c:
                    dp[a]= min(dp[a],1+dp[a-c])
                    print(dp)
        if dp[amount] == amount + 1:
            dp[amount]= -1
        return dp[amount]



# -----------------
# Tests (LeetCode examples)
# -----------------

def test_example_1():
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3
    # Explanation: 11 = 5 + 5 + 1


def test_example_2():
    sol = Solution()
    assert sol.coinChange([2], 3) == -1


def test_example_3():
    sol = Solution()
    assert sol.coinChange([1], 0) == 0

