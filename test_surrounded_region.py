# test_surrounded_regions.py
import pytest
from copy import deepcopy

def main():
    """
    Run the first example. This function is intentionally placed before the Solution
    class (per instructions) and will be called at the bottom of the file.
    """
    board = [
      ["X","X","X","X"],
      ["X","O","O","X"],
      ["X","O","O","X"],
      ["X","X","X","O"]
    ]
    expected = [
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","X"],
      ["X","X","X","O"]
    ]

    print("Input board:")
    for row in board:
        print(row)
    print()

    print("Running Solution().solve(board) ...")
    # This will raise NotImplementedError because solve is intentionally unimplemented.
    Solution().solve(board)

    print("\nResulting board:")
    for row in board:
        print(row)
    print("\nExpected board:")
    for row in expected:
        print(row)


# --- PyTest fixtures and tests ---
@pytest.fixture(params=[
    (
        [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"]
        ],
        [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","O"]
        ],
    ),
])
def case(request):
    """
    Fixture returning (board, expected) pair. Uses deepcopy so tests get fresh boards.
    """
    inp, exp = request.param
    return deepcopy(inp), deepcopy(exp)


def test_solve(case):
    """
    Single test function that uses the fixture to test Solution.solve in-place modification.
    """
    board, expected = case
    sol = Solution()
    sol.solve(board)
    assert board == expected


# --- Solution class (must be defined at the bottom) ---
class Solution:
    def solve(self, board):
        """
        Modify board in-place to capture surrounded regions.

        Intentionally unimplemented for the purposes of this exercise.
        """
        
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
       
       return board

if __name__ == "__main__":
    main()

