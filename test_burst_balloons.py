import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input, expected)
    ([3, 1, 5, 8], 167),
    ([1, 5], 10),
])
def case(request) -> Tuple[List[int], int]:
    """Fixture yielding (nums, expected) pairs."""
    return request.param


def test_max_coins(case):
    nums, expected = case
    sol = Solution()
    assert sol.maxCoins(nums) == expected


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """Return the maximum coins obtainable by bursting balloons optimally.

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

