import pytest


@pytest.fixture(params=[
    ([1, 2, 0, 1, 0], True),
    ([1, 2, 1, 0, 1], False),
])
def case(request):
    return request.param


def test_can_jump(case):
    nums, expected = case
    assert Solution().canJump(nums) == expected


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """Return True if you can reach the last index starting from index 0.
        """

        goal = len(nums)-1

        for i in range(goal-1,-1,-1):
            
            if i + nums[i] == goal:
                goal =i

        return goal == 0 


        
