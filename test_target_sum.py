import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input (nums, target), expected)
    (([1, 1, 1, 1, 1], 3), 5),
    (([1], 1), 1),
])
def case(request) -> Tuple[Tuple[List[int], int], int]:
    """Fixture yielding ((nums, target), expected) pairs."""
    return request.param


def test_find_target_sum_ways(case):
    (nums, target), expected = case
    sol = Solution()
    assert sol.findTargetSumWays(nums, target) == expected


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """Return the number of ways to assign + or - to make nums sum to target.

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

