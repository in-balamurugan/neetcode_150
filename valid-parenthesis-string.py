import pytest


@pytest.fixture(params=[
    ("((**)", True),
    ("(((*)", False),
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
    def target(self, s: str) -> bool:
       
        left =[]
        star =[]

        for i,c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)

            else:
                if not star and not left:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()

        while left and star:
            if left.pop() > star.pop():
                return False
        return not left
