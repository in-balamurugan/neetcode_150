# valid_parentheses_test.py
import pytest

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Implement this function.

        You are given a string s consisting of '(', ')', '{', '}', '[' and ']'.
        The string is valid if:
          - Every open bracket has a matching closing bracket of the same type.
          - Brackets close in the correct order.
          - Every closing bracket corresponds to an open bracket.

        Return True if valid, otherwise False.
        """
        vstack=[]
        bmap={"(":")","{":"}","[":"]"}
        for c in s:
            print(f'{c=}') 
            if c in bmap:
                vstack.append(c)
            else:
                b=vstack.pop() if vstack else '#'
                if bmap[b] != c:
                    return False
                else:
                    continue
        print(vstack)            
        if len(vstack) == 0:
            return True
        else:
            return False
# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected",
    [
        ("[]", True),        # Example 1
        ("([{}])", True),    # Example 2
        ("[(])", False),     # Example 3
    ],
)
def test_is_valid_examples(solver, s, expected):
    assert solver.isValid(s) == expected


# Allow running directly: python valid_parentheses_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

