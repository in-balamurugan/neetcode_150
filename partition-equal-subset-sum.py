"""PyTest file for Partition Equal Subset Sum.

This file contains:
- a pytest fixture with the provided test cases
- a single test function that uses the fixture
- a `main` function (placed before the Solution class) that runs the first example
- a `Solution` class at the bottom whose target method is unimplemented (raises NotImplementedError)

Do not modify this file when creating reference solutions; it's intended as a test/template file.
"""

import pytest


@pytest.fixture(params=[
    ([1, 2, 3, 4], True),
    ([1, 2, 3, 4, 5], False),
])
def case(request):
    """Fixture returning (input_list, expected_bool) pairs."""
    return request.param


def test_partition_equal_subset_sum(case):
    nums, expected = case
    sol = Solution()
    assert sol.canPartition(nums) == expected


def main():
    """Run the first example and print the result."""
    nums = [1, 2, 3, 4]
    print("Input:", nums)
    print("Output:", Solution().canPartition(nums))


class Solution:
    def canPartition(self, nums):
        """Return True if nums can be partitioned into two subsets with equal sum.

        NOTE: intentionally unimplemented — raise NotImplementedError so users
        can implement this method and run the tests.
        """
        if  sum(nums)%2:
            return False

        target = sum(nums) // 2

        dp = [False] * (target + 1)
        
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):

                dp[j] = dp[j] or dp[j - num]
                print(dp)

        return dp[target]



if __name__ == "__main__":
    main()

