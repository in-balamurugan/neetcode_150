# word_search_test.py
import pytest
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n board and a string word, return True if word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cells,
        where adjacent cells are horizontally or vertically neighboring. The same
        letter cell may not be used more than once.

        Example:
        board = [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        word = "ABCCED" -> True
        """

        if board is None or word is None or not isinstance(board, list) or not all(isinstance(row, list) for row in board) or not isinstance(word, str):
            raise TypeError("board must be a list of lists and word must be a string")
        if not board or not board[0]:
            return False

        ROWS=len(board) 
        COLS=len(board[0]) 
        
        def dfs(r,c,i):
            print(r,c,i)
            if i == len(word):
                return True
            if (r<0 or c<0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or board[r][c] == '#'):
                return False
            board[r][c] = '#'
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            board[r][c] = word[i]
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "board, word, expected",
    [
        (
            [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ],
            "ABCCED",
            True
        ),  # example 1
        (
            [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ],
            "SEE",
            True
        ),  # example 2
        (
            [
                ['A','B','C','E'],
                ['S','F','C','S'],
                ['A','D','E','E']
            ],
            "ABCB",
            False
        ),  # cannot reuse same cell
        (
            [['a']],
            "a",
            True
        ),  # single cell match (lowercase)
        (
            [['a']],
            "b",
            False
        ),  # single cell non-match
        (
            [['A','A','A','A'],
             ['A','A','A','A'],
             ['A','A','A','A']],
            "AAAAAAAAAAAAA",
            False
        ),  # longer than total cells
        (
            [['C','A','A'],
             ['A','A','A'],
             ['B','C','D']],
            "AAB",
            True
        ),  # tricky path choices
        (
            [],
            "ANY",
            False
        ),  # empty board
        (
            [['A','B'],['C','D']],
            "",
            True
        ),  # empty word -> vacuously True
    ],
)
def test_word_search_examples(solver, board, word, expected):
    assert solver.exist(board, word) == expected

def test_word_search_invalid_types(solver):
    with pytest.raises(TypeError):
        solver.exist(None, None)  # invalid inputs

def test_word_search_repeated_letters_path(solver):
    board = [
        ['A','B','C'],
        ['D','E','F'],
        ['G','H','I']
    ]
    # word requires backtracking; ensure correct True/False
    assert solver.exist(board, "AEI") is False  # diagonal not allowed
    assert solver.exist(board, "ADG") is True   # downwards column

