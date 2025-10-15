# Save as pacific_atlantic_test.py
# (If you want pytest auto-discovery, rename the file to start with "test_" when running tests.)

from typing import List
import pytest

class Solution:
    """
    Solution container for the Pacific Atlantic Water Flow problem.

    Implement `pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]`
    to return all coordinates [r, c] where water can flow to both the
    Pacific and Atlantic oceans.
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
            ROWS,COLS = len(heights),len(heights[0])
            pac,atl= set(),set()

            def dfs(r,c,visit,prevHeight):
                if((r,c) in visit or r<0 or c<0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                    return
                visit.add((r,c))
                
                dfs(r + 1, c, visit, heights[r][c])
                dfs(r - 1, c, visit, heights[r][c])
                dfs(r, c + 1, visit, heights[r][c])
                dfs(r, c - 1, visit, heights[r][c])

            for c in range(COLS):
                dfs(0, c, pac, heights[0][c])
                dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

            for r in range(ROWS):
                dfs(r, 0, pac, heights[r][0])
                dfs(r, COLS - 1, atl, heights[r][COLS - 1])

            res = []
            for r in range(ROWS):
                for c in range(COLS):
                    if (r, c) in pac and (r, c) in atl:
                        res.append([r, c])
            return res

# ---- Tests (ONLY the examples provided) ----

def test_example_1():
    sol = Solution()
    heights = [
        [4, 2, 7, 3, 4],
        [7, 4, 6, 4, 7],
        [6, 3, 5, 3, 6]
    ]
    output = sol.pacificAtlantic(heights)
    expected = [
        [0, 2], [0, 4],
        [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
        [2, 0]
    ]
    assert sorted(output) == sorted(expected)

def test_example_2():
    sol = Solution()
    heights = [[1], [1]]
    output = sol.pacificAtlantic(heights)
    expected = [[0, 0], [0, 1]]
    assert sorted(output) == sorted(expected)

