import pytest
from typing import Tuple


@pytest.fixture(params=[
    # ((s, p), expected)
    (("aa", "a"), False),
    (("aa", "a*"), True),
    (("ab", ".*"), True),
])
def case(request) -> Tuple[Tuple[str, str], bool]:
    """Fixture yielding ((s, p), expected) pairs."""
    return request.param


def test_is_match(case):
    (s, p), expected = case
    sol = Solution()
    assert sol.isMatch(s, p) == expected


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Return True if the string s matches the pattern p (with . and *).

        This method is intentionally left unimplemented for the user to fill in.
        """
        raise NotImplementedError

