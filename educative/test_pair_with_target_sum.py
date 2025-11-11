# test_pair_with_target_sum.py
# PyTest file for "Pair with Target Sum (easy)"

import pytest
from typing import List


# ---------- PyTest Fixture ----------
@pytest.fixture(
    params=[
        # (nums, target, expected_indices)
        ([1, 2, 3, 4, 6], 6, [1, 3]),   # Example 1
        ([2, 5, 9, 11], 11, [0, 2]),    # Example 2
    ]
)
def pair_cases(request):
    return request.param


# ---------- Single Test Using the Fixture ----------
def test_pair_with_target_sum(pair_cases):
    nums, target, expected = pair_cases
    sol = Solution()
    result = sol.target(nums, target)
    assert result == expected


# ---------- Main (runs first example) ----------
def main():
    nums = [1, 2, 3, 4, 6]
    target = 6
    try:
        print(Solution().target(nums, target))
    except NotImplementedError:
        # Keep execution graceful while the method is unimplemented
        print("Solution.target is not implemented yet.")




# ---------- Solution (must be last) ----------
class Solution:
    def target(self, nums: List[int], target: int) -> List[int]:
        """
        Given a sorted array `nums` and an integer `target`,
        return the indices [i, j] of two numbers such that nums[i] + nums[j] == target.
        """
        l,r =0,len(nums)-1

        while l<r:
            arr_sum = nums[l]+nums[r]
            if arr_sum == target:
                return [l,r]
            elif arr_sum > target:
                r -= 1
            elif arr_sum < target:
                l+=1




if __name__ == "__main__":
    main()
