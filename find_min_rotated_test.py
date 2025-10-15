# find_min_rotated_test.py
import pytest
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find minimum in a rotated sorted array (no duplicates).
        Implement this function.

        Example:
        Input: nums = [3,4,5,1,2]
        Output: 1
        """
        
        l,r =0,len(nums)-1

        while l<r:
            m=l+(r-l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 4, 5, 1, 2], 1),           # rotated
        ([4, 5, 6, 7, 0, 1, 2], 0),     # rotated with larger pivot
        ([11, 13, 15, 17], 11),         # not rotated (still sorted)
        ([1], 1),                       # single element
        ([2, 1], 1),                    # two elements, rotated
        ([5,6,1,2,3,4], 1),             # rotated middle
        ([1,2,3,4,5], 1),               # fully sorted ascending
    ],
)
def test_find_min_examples(solver, nums, expected):
    assert solver.findMin(nums) == expected

def test_find_min_empty(solver):
    # behavior for empty list unspecified: expect an Exception (ValueError or similar)
    with pytest.raises(Exception):
        solver.findMin([])

def test_find_min_type_errors(solver):
    with pytest.raises(TypeError):
        solver.findMin(None)  # invalid type for nums

