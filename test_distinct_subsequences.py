import pytest
from typing import Tuple


@pytest.fixture(params=[
    # ((s, t), expected)
    (("rabbbit", "rabbit"), 3),
    (("babgbag", "bag"), 5),
])
def case(request) -> Tuple[Tuple[str, str], int]:
    """Fixture yielding ((s, t), expected) pairs."""
    return request.param


def test_num_distinct(case):
    (s, t), expected = case
    sol = Solution()
    assert sol.numDistinct(s, t) == expected


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """Return the number of distinct subsequences of s equal to t.

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

