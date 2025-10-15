from typing import List
import pytest

@pytest.fixture(params=[
    ([2, 4, 1, 1, 1, 1], 2),
#    ([2, 1, 2, 1, 0], 2),
])
def case(request):
    return request.param


def test_jump_game_ii(case):
    nums, expected = case
    sol = Solution()
    assert sol.jump(nums) == expected


class Solution:
    def jump(self, nums: List[int]) -> int:
        """Return the minimum number of jumps to reach the last position.

        Method intentionally left unimplemented for test scaffolding.
        """
        
        res = 0
        l = r  = 0

        while r < len(nums) - 1 :
            farthest = 0

            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])

            print('\n',l,r)
            l = r + 1
            r = farthest
            print('\t',l,r)

            res += 1
        return res

