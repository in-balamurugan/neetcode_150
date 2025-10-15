import pytest

@pytest.fixture(params=[
    (
        [
            [0,1,1,0,1],
            [1,0,1,0,1],
            [0,1,1,0,1],
            [0,1,0,0,1]
        ],
        6
    ),
])
def case(request):
    """Fixture that yields (input_grid, expected) pairs."""
    return request.param


def test_max_area_of_island(case):
    grid, expected = case
    sol = Solution()
    assert sol.maxAreaOfIsland(grid) == expected


def main():
    """Run the first example (display only)."""
    grid = [
        [0,1,1,0,1],
        [1,0,1,0,1],
        [0,1,1,0,1],
        [0,1,0,0,1]
    ]
    expected = 6
    print("Example 1")
    print("Input grid:")
    for row in grid:
        print(row)
    print("Expected output:", expected)


# -------------------------
# Solution class at bottom
# -------------------------
class Solution:
    def maxAreaOfIsland(self, grid):
        """
        Return the maximum area of an island in the grid.
        (Method intentionally unimplemented for testing purposes.)
        """
        directions =[[1,0],[0,1],[0,-1],[-1,0]]
        ROWS,COLS = len(grid), len(grid[0])
        maxArea=0        

        def dfs(r,c):
            print(r,c)
            if r<0 or c< 0 or r>= ROWS or c >= COLS or   grid[r][c] == 0:
                return 0
            grid[r][c] = 0

            area=1
            for dr,dc in directions:
                area+=dfs(r+dr, c+dc)
            return area

        from itertools import product

        print(product(range(ROWS),range(COLS)))
        for r,c in product(range(ROWS),range(COLS)):
            if grid[r][c] == 1:
                area=dfs(r,c)
                maxArea = max(area,maxArea)

        return maxArea

    

if __name__ == "__main__":
    main()

