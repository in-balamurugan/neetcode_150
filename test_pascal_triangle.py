"""
pytest file for Pascal's Triangle problem.

Contains:
- pytest fixture with the provided test cases
- a single test function that uses the fixture
- a main() function that runs the first example (numRows = 5)
- a Solution class defined at the bottom with an unimplemented `generate` method
"""

import pytest

@pytest.fixture(params=[
    # (input_numRows, expected_output)
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (1, [[1]]),
])
def case(request):
    """Fixture yielding (input, expected) pairs for tests."""
    return request.param

def test_pascal_triangle(case):
    """Test Solution.generate against provided cases."""
    numRows, expected = case
    sol = Solution()
    assert sol.generate(numRows) == expected

def main():
    """Run the first example (numRows = 5)."""
    numRows = 5
    print("Running main example: numRows =", numRows)
    sol = Solution()
    result = sol.generate(numRows)
    print("Result:", result)

# Solution class must be defined at the bottom of the file.
class Solution:
    def generate(self, numRows: int):
        """
        Generate the first numRows of Pascal's triangle.

        This method is intentionally unimplemented for the test file.
        """
        
        res = [[1] * (i+1) for i in range(numRows)]

        for i in range(2,numRows):
            for j in range (1,i):

                res[i][j] = res[i-1][j] + res[i-1][j-1]

        return res

if __name__ == "__main__":
    main()

