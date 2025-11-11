"""
Remove Duplicates (easy)

Problem Statement:
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

Examples:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

import pytest


# ------------------------
# Main runner (runs first example)
# ------------------------
def main():
    example_input = [2, 3, 3, 3, 6, 9, 9]
    expected_output = 4
    print("Running first example...")
    print(f"Input: {example_input}")
    try:
        result = Solution().remove_duplicates(example_input.copy())
        print(f"Output: {result}")
        print(f"Expected: {expected_output}")
    except NotImplementedError:
        print("remove_duplicates is not implemented yet.")




# ------------------------
# PyTest setup
# ------------------------

# Single fixture with all (input, expected) pairs provided by the user
@pytest.fixture(
    params=[
        ([2, 3, 3, 3, 6, 9, 9], 4),  # Example 1
        ([2, 2, 2, 11], 2),          # Example 2
    ]
)
def cases(request):
    return request.param


# One test function that uses the fixture to test the method
def test_remove_duplicates(cases):
    nums, expected = cases
    sol = Solution()
    assert sol.remove_duplicates(nums) == expected


# ------------------------
# Solution (unimplemented)
# ------------------------
class Solution:
    def remove_duplicates(self, nums):
        """
        Remove duplicates from a sorted list in place and return the new length.
        This method is intentionally left unimplemented.
        """
        
        l = 1
        
        for r in range(1,len(nums)):

            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1


        return l





if __name__ == "__main__":
    main()
