"""
pytest file for: given a text document (plain text), find the largest cluster of words (cluster
connectivity is 4-directional: up, down, left, right) where a cluster consists of adjacent words
in the text layout (the problem is analogous to "max area of island").

This file provides:
 - TEST_CASES: a list of (input_text, expected) pairs.  <-- FILL THIS with the cases you will provide.
 - A pytest fixture that yields each case.
 - A single test function that tests Solution().target(input_text) == expected.
 - A main() function that runs the first example (if present) and prints input/expected/output.
 - A single Solution class at the bottom with an unimplemented target() method that raises NotImplementedError.

Notes:
 - The precise parsing / grid formation from the input text is intentionally NOT implemented here;
   the Solution.target method is left unimplemented as requested.
 - Add your test cases to TEST_CASES; this file will run them with pytest.
"""

import pytest
from typing import Tuple, List

# ---------------------------
# PLACEHOLDER FOR TEST CASES
# ---------------------------
# Fill TEST_CASES with the (input_text, expected) pairs you will provide.
# Each input_text should be a single string representing the contents of a .txt document.
# expected should be the expected integer result for Solution().target(input_text).
TEST_CASES = [
    (
        """Lorem ipsum dolor sit amet
Lorem ipsum dolor sit amet
Lorem lorem ipsum lorem amet
dolor sit amet lorem ipsum""",
        17,  # all words with >=4 letters form one large cluster
    ),
]


# ---------------------------
# Pytest fixture & test
# ---------------------------
@pytest.fixture(params=TEST_CASES)
def case(request):
    """
    Pytest fixture yielding each (input_text, expected) pair from TEST_CASES.
    The user requested a single test function that uses this fixture.
    """
    return request.param

def test_target_case(case):
    """
    Single test function that uses the above fixture to test Solution.target.
    """
    input_text, expected = case
    sol = Solution()
    assert sol.target(input_text) == expected

# ---------------------------
# Main to run first example
# ---------------------------
def main():
    """
    If there is at least one test case in TEST_CASES, run the first one and print input, expected, and output.
    This does not implement the algorithm; it simply demonstrates how main would call the target method.
    """
    if not TEST_CASES:
        print("No test cases provided in TEST_CASES. Please add (input_text, expected) pairs.")
        return

    input_text, expected = TEST_CASES[0]
    print("=== Running first example from TEST_CASES ===")
    print("Input text (truncated preview):")
    # Print a small preview for readability
    preview = input_text if len(input_text) <= 400 else input_text[:400] + " ... [truncated]"
    print(preview)
    print("\nExpected:", expected)
    try:
        output = Solution().target(input_text)
        print("Output:", output)
    except NotImplementedError:
        print("Solution.target is not implemented. It raised NotImplementedError as expected.")
    except Exception as e:
        print("Solution.target raised an unexpected exception:", repr(e))

# ------------------------------------------------
# Solution class (single class, at bottom of file)
# ------------------------------------------------
class Solution:
    """
    Solution class containing the target method.

    Problem summary (for implementer):
    - Input: the text contents of a .txt document (string).
    - The document should be interpreted as paragraphs / lines forming a 2D word layout.
      Words are tokens separated by whitespace. You should arrange words in the same layout
      as they appear in the text (line breaks matter).
    - A cluster is formed by adjacent words (up, down, left, right).
    - The goal: return the size (number of words) of the largest cluster whose size is > 4.
      (Interpretation: you may return the size of the largest cluster; the calling tests
      will check that against expected.)
    - This method is intentionally left unimplemented and must raise NotImplementedError.
    """
    def target(self, input_text: str) -> int:
        """
        Target method to implement the algorithm.

        Args:
            input_text: str -- full contents of the text document.

        Returns:
            int -- size of the largest cluster (number of words).

        NOTE: per instructions this method must be left unimplemented in this file.
        """
        





    grid=[[]]

        i=0
        grid = [line.split() for line in input_text.splitlines()]

        print(grid)

        ROWS,COLS =len(grid),len(grid[0])
        visit =set()

        def dfs(r,c):
            
            if (r < 0 or r == ROWS or c < 0 or c == COLS or len(grid[r][c]) <4 or (r, c) in visit):
                return 0

            visit.add((r,c))

            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        max_cluster = 0
        for r in range(ROWS):
            for c in range(COLS):
                 max_cluster = max(max_cluster,dfs(r,c))

        return max_cluster




# Call main when run as a script (but not on import for pytest collection)
if __name__ == "__main__":
    main()

