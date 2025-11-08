# test_smallest_subarray_with_given_sum.py
from typing import List, Tuple
import pytest


# -------------------------
# Problem: Smallest Subarray with a given sum (easy)
# -------------------------
# Given an array of positive numbers and a positive number S,
# find the length of the smallest contiguous subarray whose sum
# is greater than or equal to S. Return 0, if no such subarray exists.
#
# Examples:
# 1) Input: [2, 1, 5, 2, 3, 2], S=7  -> Output: 2
# 2) Input: [2, 1, 5, 2, 8], S=7     -> Output: 1
# 3) Input: [3, 4, 1, 1, 6], S=8     -> Output: 3


@pytest.fixture(
    params=[
        (([2, 1, 5, 2, 3, 2], 7), 2),  # [5,2]
        (([2, 1, 5, 2, 8], 7), 1),     # [8]
        (([3, 4, 1, 1, 6], 8), 3),     # [3,4,1] or [1,1,6]
    ]
)
def sample_cases(request):
    """Parameterized fixture yielding ((arr, S), expected_length)."""
    return request.param


def test_smallest_subarray_len(sample_cases):
    """Single test function using the fixture to validate the method."""
    (arr, s), expected = sample_cases
    sol = Solution()
    assert sol.smallest_subarray_len(arr, s) == expected


def main():
    """Runs the first example."""
    arr = [2, 1, 5, 2, 3, 2]
    S = 7
    sol = Solution()
    result = sol.smallest_subarray_len(arr, S)
    print(f"Input: {arr}, S={S} -> Smallest length: {result}")



# -------------------------
# Leave the Solution class at the bottom.
# The target method is intentionally unimplemented.
# -------------------------
class Solution:
    def smallest_subarray_len(self, arr: List[int], S: int) -> int:
        """
        Returns the length of the smallest contiguous subarray with sum >= S.
        If no such subarray exists, return 0.
        """
        
        l=0
        window_sum = 0
        min_length=float('inf')

        for r in range(len(arr)):

            window_sum += arr[r]

            while window_sum >= S:
                min_length=min(min_length,r-l+1)
                window_sum -= arr[l]
                l += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length




if __name__ == "__main__":
    main()
