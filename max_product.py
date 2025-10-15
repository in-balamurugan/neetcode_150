# Save this file as "max_product_test.py"
# (Note: per your request, the filename does NOT start with "test" in this comment.
#  If you want pytest to auto-discover, rename it to start with "test_" when running tests.)

import pytest
from typing import List

class Solution:
    """
    Solution container for the Maximum Product Subarray problem.

    Implement `maxProduct(self, nums: List[int]) -> int` to return the largest product
    of any contiguous, non-empty subarray of nums.
    """
    def maxProduct(self, nums: List[int]) -> int:
        curMin,curMax = 0,0
        res = nums[0]

        for num in nums:
            tmp = curMax * num
            curMax = max(num*curMax,num*curMin,num)
            curMin = min(num*tmp,num*curMin,num)
            res=max(res,curMax)
        return res

# --- Tests (only the examples you provided) ---

def test_example_1():
    sol = Solution()
    assert sol.maxProduct([1, 2, -3, 4]) == 4


def test_example_2():
    sol = Solution()
    assert sol.maxProduct([-2, -1]) == 2

