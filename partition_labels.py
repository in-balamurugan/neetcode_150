import pytest
from typing import List


@pytest.fixture(params=[
    ("xyxxyzbzbbisl", [5, 5, 1, 1, 1]),
    ("abcabc", [6]),
])
def case(request):
    s, expected = request.param
    return s, expected


def test_target(case):
    s, expected = case
    sol = Solution()
    assert sol.target(s) == expected


# Single Solution class at the bottom as requested
class Solution:
    def target(self, s: str) -> List[int]:
        """Unimplemented: should return partition sizes for the input string s.
        Raise NotImplementedError until implemented.
        """
        
        rightmost ={c:i for i,c in enumerate(s)}
        
        left,right =0,0

        result = []
        for i, letter in enumerate(s):

            right = max(right, rightmost[letter])

            if i == right:
                result += [right-left +1]
                left = i+1

        return result
