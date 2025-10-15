# test_number_of_islands.py
import pytest
from typing import List, Tuple

def main():
    # First example from the prompt
    grid = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    try:
        result = Solution().numIslands(grid)  # Solution defined below (method intentionally unimplemented)
        print("Number of islands (example 1):", result)
    except NotImplementedError:
        print("numIslands is not implemented yet (main ran the first example).")

# PyTest fixture holding exactly the given (input, expected) pairs
@pytest.fixture(params=[
    (
        [
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        1
    ),
    (
        [
            ["1","1","0","0","1"],
            ["1","1","0","0","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        4
    )
])
def case(request) -> Tuple[List[List[str]], int]:
    return request.param

def test_num_islands(case):
    grid, expected = case
    sol = Solution()
    assert sol.numIslands(grid) == expected

# Solution class must be defined at the bottom with the target method unimplemented
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands in the given grid where '1' is land and '0' is water.

        This method is intentionally left unimplemented for the exercise and should raise
        NotImplementedError until implemented by the user.
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        islands =0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):

            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c] == "0":
                return

            print(r,c)
            grid[r][c] = "0"

            for rd,cd in directions:
                dfs(r+rd,c+cd)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands
            




# Call main at bottom as requested
if __name__ == "__main__":
    main()

