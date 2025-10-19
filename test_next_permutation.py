"""
pytest file for Next Permutation problem.

Contains:
- pytest fixture with the provided test cases
- a single test function that uses the fixture
- a main() function that runs the first example (nums = [1, 2, 3])
- a Solution class defined at the bottom with an unimplemented `nextPermutation` method
"""

import pytest
from typing import List

@pytest.fixture(params=[
    # (input_nums, expected_result_after_call)
    ([1, 2, 3], [1, 3, 2]),
    ([3, 2, 1], [1, 2, 3]),
])
def case(request):
    """Fixture yielding (input_list_copy, expected) pairs for tests."""
    inp, expected = request.param
    # return a copy of the input because nextPermutation mutates in-place
    return inp.copy(), expected

def test_next_permutation(case):
    """Test Solution.nextPermutation mutates the list to the expected next permutation."""
    nums, expected = case
    sol = Solution()
    sol.nextPermutation(nums)
    assert nums == expected

def main():
    """Run the first example (nums = [1, 2, 3])."""
    nums = [1, 2, 3]
    print("Running main example: nums =", nums)
    sol = Solution()
    sol.nextPermutation(nums)
    print("Result:", nums)

# Solution class must be defined at the bottom of the file.
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Rearranges numbers into the lexicographically next greater permutation.

        This method is intentionally unimplemented for the test file.
        It should modify `nums` in-place and return None.
        """
        raise NotImplementedError


if __name__ == "__main__":
    main()

