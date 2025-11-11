# test_triplet_sum_close_to_target.py
# PyTest file for "Triplet Sum Close to Target"

import pytest
from typing import List


# ---------- PyTest Fixture ----------
@pytest.fixture(
    params=[
        # (nums, target, expected_sum)
        ([-2, 0, 1, 2], 2, 1),     # Example 1
        ([-3, -1, 1, 2], 1, 0),    # Example 2
        ([1, 0, 1, 1], 100, 3),    # Example 3
    ]
)
def triplet_close_cases(request):
    return request.param


# ---------- Single Test Using the Fixture ----------
def test_triplet_sum_close_to_target(triplet_close_cases):
    nums, target, expected = triplet_close_cases
    sol = Solution()
    result = sol.target(nums, target)
    assert result == expected


# ---------- Main (runs first example) ----------
def main():
    nums = [-2, 0, 1, 2]
    target = 2
    try:
        print(Solution().target(nums, target))
    except NotImplementedError:
        # Keep execution graceful while the method is unimplemented
        print("Solution.target is not implemented yet.")




# ---------- Solution (must be last) ----------
class Solution:
    def target(self, nums: List[int], target_sum: int) -> List[int]:
        nums.sort()
        l = len(nums) - 1

        closest_sum = float("inf")
        closest_triplet = None          

        for i in range(l - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = l

            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                # update best match
                if abs(curr - target_sum) < abs(closest_sum - target_sum):
                    closest_sum = curr
                    closest_triplet = [nums[i], nums[j], nums[k]]

                # exact match → can't get closer
                if curr == target_sum:
                    return [nums[i], nums[j], nums[k]]

                elif curr > target_sum:
                    k -= 1
                else:
                    j += 1

        return closest_sum



if __name__ == "__main__":
    main()
