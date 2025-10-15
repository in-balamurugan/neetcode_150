import pytest
from typing import Tuple


@pytest.fixture(params=[
    # ((word1, word2), expected)
    (("horse", "ros"), 3),
    (("intention", "execution"), 5),
])
def case(request) -> Tuple[Tuple[str, str], int]:
    """Fixture yielding ((word1, word2), expected) pairs."""
    return request.param


def test_min_distance(case):
    (word1, word2), expected = case
    sol = Solution()
    assert sol.minDistance(word1, word2) == expected


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of operations to convert word1 to word2.

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

