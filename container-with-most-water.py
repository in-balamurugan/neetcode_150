# max_area_test.py
import pytest
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Implement this function.

        Given an integer array `height` of length n where the i-th vertical line is
        drawn from (i, 0) to (i, height[i]), find two lines that together with the x-axis
        form a container such that the container contains the most water.

        Return the maximum amount of water a container can store (area). You may not slant the container.
        """

        l,r = 0,len(height)-1
        maxarea= 0
        while l<r:

            print(l,r,height)            
            area = min(height[l],height[r]) *(r-l) 
            maxarea = max(area,maxarea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
            


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "height, expected",
    [
        ([1,8,6,2,5,4,8,3,7], 49),  # Example 1
        ([1,1], 1),                # Example 2
    ],
)
def test_max_area_examples(solver, height, expected):
    assert solver.maxArea(height) == expected

# Allow running directly: python max_area_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

