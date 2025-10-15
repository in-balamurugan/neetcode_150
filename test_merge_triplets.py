import pytest
from typing import List


@pytest.fixture(params=[
    ((([1, 2, 3], [7, 1, 1]), [7, 2, 3]), True),
    ((([2, 5, 6], [1, 4, 4], [5, 7, 5]), [5, 4, 6]), False),
])
def case(request):
    (triplets, target), expected = request.param
    return triplets, target, expected


def test_target(case):
    triplets, target, expected = case
    sol = Solution()
    assert sol.target(list(triplets), list(target)) == expected


# Single Solution class at the bottom as requested
class Solution:
    def target(self, triplets: List[List[int]], target: List[int]) -> bool:
        """Unimplemented: should return True if target can be obtained from triplets.
        Raise NotImplementedError until implemented.
        """
        raise NotImplementedError

