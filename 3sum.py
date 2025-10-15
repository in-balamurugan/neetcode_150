# three_sum_test.py
import pytest
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Implement this function.

        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        The solution set must not contain duplicate triplets. Order of triplets and order
        within each triplet does not matter.
        """
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if a>0:
                break
            if i>0 and a == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            
            while l<r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1

                    while nums[l] == nums[l-1] and l<r:
                               l += 1
        return res


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "nums, expected_sets",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # Example 1
        ([0, 1, 1], []),                                     # Example 2
        ([0, 0, 0], [[0, 0, 0]]),                            # Example 3
    ],
)
def test_three_sum_examples(solver, nums, expected_sets):
    result = solver.threeSum(nums)

    # Normalize: sort each triplet and then sort list of triplets for comparison
    def normalize(list_of_lists):
        return sorted([sorted(trip) for trip in list_of_lists])

    assert normalize(result) == normalize(expected_sets)

# Allow running with: python three_sum_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

