# test_set_matrix_zeroes.py
from typing import List, Tuple
import pytest

"""
Set Matrix Zeroes
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:
Input: matrix = [
  [0,1],
  [1,0]
]
Output: [
  [0,0],
  [0,0]
]

Example 2:
Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]
Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
"""

@pytest.fixture(params=[
    # (input_matrix, expected_matrix)
    (
        [[0, 1],
         [1, 0]],
        [[0, 0],
         [0, 0]]
    ),
    (
        [[1, 2, 3],
         [4, 0, 5],
         [6, 7, 8]],
        [[1, 0, 3],
         [0, 0, 0],
         [6, 0, 8]]
    ),
])
def case(request) -> Tuple[List[List[int]], List[List[int]]]:
    # The fixture yields the (input_matrix, expected_matrix) pair.
    # Tests are expected to mutate the input_matrix in-place.
    return request.param

def test_set_matrix_zeroes(case):
    matrix, expected = case
    sol = Solution()
    # The target method should update matrix in-place.
    sol.setZeroes(matrix)
    assert matrix == expected

# A small main function to show the first example (does not call the unimplemented method)
def main():
    example_input = [
        [0, 1],
        [1, 0]
    ]
    example_expected = [
        [0, 0],
        [0, 0]
    ]
    print("First example input:")
    for row in example_input:
        print(row)
    print("\nExpected output after running Solution.setZeroes:")
    for row in example_expected:
        print(row)

if __name__ == "__main__":
    main()

# --- Solution class must be defined at the bottom of the file ---
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify matrix in-place so that if an element is 0, its entire row and column are set to 0.
        This method is intentionally left unimplemented for the user to fill in.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

