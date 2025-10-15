import pytest
from typing import List, Tuple

@pytest.fixture(params=[
    # (height, expected)
    ([0, 2, 0, 3, 1, 0, 1, 3, 2, 1], 9),
])
def case(request) -> Tuple[List[int], int]:
    return request.param


def test_trap(case):
    height, expected = case
    sol = Solution()
    assert sol.trap(height) == expected


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0, len(height)-1
        leftMax,rightMax = height[l], height[r]
        res=0

        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l] 
            else :
                r -= 1
                rightMax = max(rightMax,height[r])
                res += rightMax - height[r]
        
        return res
