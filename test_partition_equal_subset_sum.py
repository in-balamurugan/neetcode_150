import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input, expected)
    ([1, 5, 11, 5], True),
    ([1, 2, 3, 5], False),
])
def case(request) -> Tuple[List[int], bool]:
    """Fixture yielding (nums, expected) pairs."""
    return request.param


def test_can_partition(case):
    nums, expected = case
    sol = Solution()
    assert sol.canPartition(nums) == expected


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Return True if nums can be partitioned into two subsets with equal sum.

        This method is intentionally left unimplemented for the user to fill in.
        """
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            newDp=set()

            for t in dp:
                if (t + nums[i]) == target:
                    return True

                newDp.add(t+nums[i])
                newDp.add(t)
            
            dp=newDp
        return False
