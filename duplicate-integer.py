
#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return not len(s) ==  len(nums)



if __name__ == '__main__':
    s=Solution()
    assert s.hasDuplicate([1, 2, 3, 1]) == True

    assert s.hasDuplicate([1, 2, 3]) == 0
