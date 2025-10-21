import pytest
from typing import List, Tuple


def main() -> None:
    """Run the first example and print input and expected output.
    This function does not call the unimplemented Solution.findMin method.
    """
    nums = [3, 4, 5, 6, 1, 2]
    expected = 1
    print("Example 1")
    print(f"Input: {nums}")
    print(f"Expected output: {expected}")


# Test data fixture: contains only the provided examples
@pytest.fixture(params=[
    ([3, 4, 5, 6, 1, 2], 1),
    ([4, 5, 0, 1, 2, 3], 0),
    ([4, 5, 6, 7], 4),
])
def example_pair(request) -> Tuple[List[int], int]:
    return request.param


def test_find_min(example_pair: Tuple[List[int], int]) -> None:
    nums, expected = example_pair
    sol = Solution()
    assert sol.findMin(nums) == expected


# Solution class must be defined at the bottom of the file.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Find the minimum element in a rotated sorted array.

        This method is intentionally unimplemented for the test scaffold.
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

# Call main at the bottom as requested
main()
