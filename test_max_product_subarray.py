import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input, expected)
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
])
def case(request) -> Tuple[List[int], int]:
    """Fixture yielding (nums, expected) pairs."""
    return request.param


def test_max_product(case):
    nums, expected = case
    sol = Solution()
    assert sol.maxProduct(nums) == expected


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """Finds the largest product of a contiguous subarray.

        This method is intentionally left unimplemented for the user to fill in.
        """
        
        res =nums[0]
        curMin,curMax =1,1

        for num in nums:

            tmp = num*curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = max(tmp,num*curMin, num)
            res = max(res, curMax)

        return res
