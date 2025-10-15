import pytest
from typing import Tuple


@pytest.fixture(params=[
    # ((s1, s2, s3), expected)
    (("aabcc", "dbbca", "aadbbcbcac"), True),
    (("aabcc", "dbbca", "aadbbbaccc"), False),
    (("", "", ""), True),
])
def case(request) -> Tuple[Tuple[str, str, str], bool]:
    """Fixture yielding ((s1, s2, s3), expected) pairs."""
    return request.param


def test_is_interleave(case):
    (s1, s2, s3), expected = case
    sol = Solution()
    assert sol.isInterleave(s1, s2, s3) == expected


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Return True if s3 is an interleaving of s1 and s2.

        This method is intentionally left unimplemented for the user to fill in.
        """

        def dfs(i,j,k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i <len(s1) and s1[i]  == s3[k]:
                if dfs(i+1,j,k+1):
                    return True

            if i< len(s2) and s2[j] == s3[k]:
                if dfs(i,j+1,k+1):
                    return True

            return False

        return dfs(0,0,0)
