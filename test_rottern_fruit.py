import copy
import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    (
        [[1, 1, 0], [0, 1, 1], [0, 1, 2]],
        4,
    ),
    (
        [[1, 0, 1], [0, 2, 0], [1, 0, 1]],
        -1,
    ),
])
def cases(request) -> Tuple[List[List[int]], int]:
    grid, expected = request.param
    return copy.deepcopy(grid), expected


def test_rotting_fruit(cases):
    grid, expected = cases
    sol = Solution()
    result = sol.orangesRotting(grid)
    assert result == expected


# A small main to run the first example. Placed before Solution as requested.
def main():
    example_grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
    print("Input grid:")
    for row in example_grid:
        print(row)
    try:
        ans = Solution().orangesRotting(example_grid)
    except NotImplementedError:
        print("orangesRotting is not yet implemented")
        return
    print("Result:", ans)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Return minimum minutes until no fresh fruits remain, or -1 if impossible.

        This method is intentionally left unimplemented for the tests.
        """
        
        from collections import deque
        
        q = deque()
        fresh = 0
        time  = 0
        directions =[[1,0],[0,1],[-1,0],[0,-1]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                        fresh += 1
        
        while fresh >0 and q:

            length = len(q)

            for i in range(length):
                r,c = q.popleft()

                for dr,dc in directions:
                    row,col = r+dr,c+dc

                    if row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]  == 1:
                           grid[row][col] = 2
                           fresh -=   1
                           q.append((row,col))
            time += 1

        return time if fresh == 0 else -1

            

        

if __name__ == "__main__":
    main()

