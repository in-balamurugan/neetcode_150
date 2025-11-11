# test_three_sum.py
# PyTest file for "Find all unique triplets that add up to zero"

import pytest
from typing import List


# ---------- PyTest Fixture ----------
@pytest.fixture(
    params=[
        # (nums, expected_triplets)
        ([-3, 0, 1, 2, -1, 1, -2], [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]),  # Example 1
        ([-5, 2, -1, -2, 3], [[-5, 2, 3], [-2, -1, 3]]),                                # Example 2
    ]
)
def triplet_cases(request):
    return request.param


# ---------- Single Test Using the Fixture ----------
def test_three_sum(triplet_cases):
    nums, expected = triplet_cases
    sol = Solution()
    result = sol.target(nums)
    assert result == expected


# ---------- Main (runs first example) ----------
def main():
    nums = [-3, 0, 1, 2, -1, 1, -2]
    try:
        print(Solution().target(nums))
    except NotImplementedError:
        # Keep execution graceful while the method is unimplemented
        print("Solution.target is not implemented yet.")


# ---------- Solution (must be last) ----------
class Solution:
    def target(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array of unsorted numbers, return all unique triplets [a, b, c]
        such that a + b + c == 0. The order of triplets and the order within
        each triplet is unspecified.
        """
        res=[]
        l=len(nums)-1

        nums.sort()
        for i in range(l-1):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            j=i+1
            k=l
            
            while j<k:
                target = nums[i] +nums[j]+nums[k]

                if target == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1


                if target >0:
                    k -= 1
                elif target <0:
                    j += 1

                
    
        return res 

if __name__ == "__main__":
    main()
