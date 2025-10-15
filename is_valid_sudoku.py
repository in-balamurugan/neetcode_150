import pytest
from collections import defaultdict

@pytest.fixture(params=[
    (
        [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","8",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]],
        True
    ),
    (
        [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","1",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]],
        False
    )
])
def case(request):
    """Fixture providing (board, expected) pairs."""
    return request.param

def test_is_valid_sudoku(case):
    board, expected = case
    sol = Solution()
    assert sol.isValidSudoku(board) == expected

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        (Method intentionally left unimplemented for testing.)
        """

        
        cols= defaultdict(set)
        rows=defaultdict(set)

        squares=defaultdict(set)
        
        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3,c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])

        return True

