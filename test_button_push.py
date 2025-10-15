# test_letter_combinations.py
from typing import List, Tuple
import pytest

# --- tests ---------------------------------------------------------------

@pytest.fixture(params=[
    # Example 1
    ("34", ["dg","dh","di","eg","eh","ei","fg","fh","fi"]),
    # Example 2
    ("", []),
])
def case(request) -> Tuple[str, List[str]]:
    """Fixture providing (input, expected) pairs."""
    return request.param

def _sorted_list(lst: List[str]) -> List[str]:
    """Return a sorted copy of the list (stable for comparison)."""
    return sorted(lst)

def test_letter_combinations(case):
    digits, expected = case
    sol = Solution()
    result = sol.letterCombinations(digits)
    assert _sorted_list(result) == _sorted_list(expected)


# --- main (runs the first example when executed as a script) -------------

def main() -> None:
    """Run the first example and print the result (used when executed as a script)."""
    digits = "34"
    print("Input:", digits)
    sol = Solution()
    print("Output:", sol.letterCombinations(digits))


# --- solution (left unimplemented as requested) ---------------------------

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Return all possible letter combinations that the input digits could represent.
        (Intentionally unimplemented for the testing task.)
        """
        res =[]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i,curStr):

            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                dfs(i+1, curStr +c )

        if digits:
            dfs(0,"")

        return res

if __name__ == "__main__":
    main()

