# Save this file as "lis_test.py"
# (Note: the filename in this comment does NOT start with "test_".
#  If you want pytest auto-discovery, name the file starting with "test_".)

from typing import List
import pytest
from bisect import bisect_left

class Solution:
    """
    Solution container for Longest Increasing Subsequence.

    Implement `lengthOfLIS(self, nums: List[int]) -> int` to return the length
    of the longest strictly increasing subsequence in nums.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        sub.append(nums[0])


        for i in range(1,len(nums)):
            i=bisect_left(sub,num)

            if i == len(sub):
                sub.append(num)
            else:
                sub[i]=num
            return len(sub)

# ---- Tests (common examples) ----

def test_example_1():
    sol = Solution()
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    # One LIS is [2,3,7,101]

def test_example_2():
    sol = Solution()
    assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    # One LIS is [0,1,2,3]

