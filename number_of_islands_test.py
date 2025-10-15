# Save as number_of_islands_test.py
# (If you want pytest auto-discovery, rename the file to start with "test_" when running tests.)

from typing import List
import pytest

class Solution:
    """
    Solution container for the Number of Islands problem.

    Implement `numIslands(self, grid: List[List[str]]) -> int` to return the
    number of islands in the given grid.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid),len(grid[0])
        islands=0

        def dfs(r,c):

            print(r,c)
            if (r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == "0"):
                return
            grid[r][c]= "0"
            for r1,c1 in directions:
                dfs(r+r1,c+c1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands+=1
        return islands


# ---- Tests (ONLY the examples provided) ----

def test_example_1():
    sol = Solution()
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert sol.numIslands(grid) == 1

def test_example_2():
    sol = Solution()
    grid = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert sol.numIslands(grid) == 4

