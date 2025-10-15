import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    # (input, expected)
    ([[9,9,4],[6,6,8],[2,1,1]], 4),
    ([[3,4,5],[3,2,6],[2,2,1]], 4),
    ([[1]], 1),
])
def case(request) -> Tuple[List[List[int]], int]:
    """Fixture yielding (matrix, expected) pairs."""
    return request.param


def test_longest_increasing_path(case):
    matrix, expected = case
    sol = Solution()
    assert sol.longestIncreasingPath(matrix) == expected


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Return the length of the longest increasing path in the matrix.

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

