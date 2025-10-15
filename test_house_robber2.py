# test_house_robber2.py
import pytest
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber II (circular houses).
        Given nums where nums[i] is the amount at house i and houses are in a circle,
        return the maximum amount you can rob without robbing adjacent houses
        (first and last are adjacent).
        """

        def helper(nums):
            rob1,rob2=0,0
            
            for num in nums:
                temp=max(num+rob1,rob2)
                rob1=rob2
                rob2=temp
            return rob2

        return max(nums[0] , helper(nums[1:]) , helper(nums[:-1]))



# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Provided examples
        ([1, 1, 3, 3], 4),
        ([2, 9, 8, 3, 6], 15),

        # Circular examples
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),

    ],
)
def test_rob_circle(solver, nums, expected):
    assert solver.rob(list(nums)) == expected


# Allow running directly: python test_house_robber2.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

