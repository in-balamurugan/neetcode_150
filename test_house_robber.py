# test_house_robber.py
import pytest
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        You are given an integer array nums where nums[i] represents the amount
        of money the ith house has. The houses are arranged in a straight line,
        i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

        You are planning to rob money from the houses, but you cannot rob two
        adjacent houses because the security system will automatically alert
        the police if two adjacent houses were both broken into.

        Return the maximum amount of money you can rob without alerting the police.

        Constraints:
          1 <= nums.length <= 100
          0 <= nums[i] <= 100
        """
        rob1,rob2=0,0

        for num in nums:
            temp=max(num+rob1,rob2)
            rob1 = rob2
            rob2=temp
        return rob2

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Example 1
        ([1, 1, 3, 3], 4),          # 1 + 3 = 4
        # Example 2
        ([2, 9, 8, 3, 6], 16),     # 2 + 8 + 6 = 16
        # Edge cases
        ([0], 0),
        ([5], 5),
        ([2, 1], 2),
        ([1, 2, 3, 1], 4),         # 1 + 3 = 4
        ([2, 7, 9, 3, 1], 12),     # 2 + 9 + 1 = 12
        ([100] * 100, 5000),       # alternating picks from 100s: 50 * 100 = 5000
        ([0, 0, 0, 0], 0),
        ([1, 100, 1, 100, 1], 200), # choose both 100s
    ],
)
def test_rob(solver, nums, expected):
    assert solver.rob(list(nums)) == expected


# Allow running directly: python test_house_robber.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

