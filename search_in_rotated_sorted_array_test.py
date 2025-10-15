# search_in_rotated_sorted_array_test.py
import pytest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Search in Rotated Sorted Array.

        You are given an integer array nums sorted in ascending order (with distinct values),
        which is rotated at some pivot unknown to you beforehand.

        Implement this function to return the index of target if it is in nums, 
        or -1 if it is not in nums.

        Example:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        """
        


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4,5,6,7,0,1,2], 0, 4),      # target at rotation point
        ([4,5,6,7,0,1,2], 3, -1),     # target not in array
        ([1], 0, -1),                 # single element, not found
        ([1], 1, 0),                  # single element, found
        ([1,3], 3, 1),                # small rotated case
        ([6,7,1,2,3,4,5], 6, 0),      # target at beginning
        ([6,7,1,2,3,4,5], 5, 6),      # target at end
        ([6,7,1,2,3,4,5], 2, 3),      # target in middle after rotation
        ([5,1,3], 5, 0),              # odd length
    ],
)
def test_search_examples(solver, nums, target, expected):
    assert solver.search(nums, target) == expected

def test_search_invalid_types(solver):
    with pytest.raises(TypeError):
        solver.search(None, 3)

def test_search_empty_array(solver):
    assert solver.search([], 10) == -1

