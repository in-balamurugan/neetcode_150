from typing import List
import pytest


@pytest.fixture(params=[
    ([2, -3, 4, -2, 2, 1, -1, 4], 8),
    ([-1], -1),
])
def case(request):
    return request.param


def test_max_subarray(case):
    nums, expected = case
    sol = Solution()
    assert sol.maxSubArray(nums) == expected


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Find the subarray with the largest sum and return the sum.

        Method intentionally left unimplemented for test scaffolding.
        """
        
        max_sum,cur_sum = nums[0],0
        for n in nums:
            if cur_sum < 0:
                cur_sum =0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)

        return max_sum

