import pytest
from typing import List, Tuple

# Example main to run the first example (prints result or a clear message if unimplemented)
def main() -> None:
    digits = "34"
    print(f"Running main example with digits=\"{digits}\"")
    sol = Solution()
    try:
        output = sol.letterCombinations(digits)
        print("Output:", output)
    except NotImplementedError:
        print("Solution.letterCombinations is not implemented.")


# Pytest fixture holding input/expected pairs (includes the two provided examples and a couple of additional test cases)
@pytest.fixture(params=[
    ("34", ["dg","dh","di","eg","eh","ei","fg","fh","fi"]),  # provided example 1
    ("", []),  # provided example 2
    ("2", ["a","b","c"]),  # additional simple test
    ("79", [
        "pw","px","py","pz",
        "qw","qx","qy","qz",
        "rw","rx","ry","rz",
        "sw","sx","sy","sz",
    ])  # additional test covering 4-letter mappings
])
def letter_cases(request) -> Tuple[str, List[str]]:
    return request.param


# Single test function that uses the fixture to test Solution.letterCombinations
def test_letter_combinations(letter_cases: Tuple[str, List[str]]) -> None:
    digits, expected = letter_cases
    sol = Solution()
    result = sol.letterCombinations(digits)
    assert result == expected


# Solution class must be present at the bottom. The target method is intentionally unimplemented.
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Given a string containing digits from 2-9 inclusive, return all possible letter combinations.

        This method is intentionally unimplemented for the purposes of the exercise.
        """

        if not digits: return []
        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        for digit in digits:
            tmp = []
            for curStr in res:
                for c in digitToChar[digit]:
                    tmp.append(curStr + c)
            res = tmp
        return res

if __name__ == "__main__":
    # call main when script is executed directly
    main()

