import pytest
from typing import List
import copy

INF = 2147483647

# Main runner that demonstrates the first example.
def main():
    example = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    print("Input (example 1):")
    for row in example:
        print(row)
    try:
        Solution().islandsAndTreasure(example)
        print("After running Solution.islandsAndTreasure:")
        for row in example:
            print(row)
    except NotImplementedError:
        print("Solution.islandsAndTreasure is not implemented.")


# PyTest fixtures and tests
@pytest.fixture(params=[
    # Example 1
    (
        [
            [INF, -1, 0, INF],
            [INF, INF, INF, -1],
            [INF, -1, INF, -1],
            [0, -1, INF, INF],
        ],
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    ),
    # Example 2
    (
        [
            [0, -1],
            [INF, INF],
        ],
        [
            [0, -1],
            [1, 2],
        ],
    ),
])
def case(request):
    # return deep copies so tests do not share mutable state
    inp, expected = request.param
    return copy.deepcopy(inp), copy.deepcopy(expected)


def test_islands_and_treasure(case):
    inp, expected = case
    sol = Solution()
    # operate on a copy since method is expected to modify in-place
    grid = copy.deepcopy(inp)
    sol.islandsAndTreasure(grid)
    assert grid == expected


# Solution class (target method unimplemented)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Modify the grid in-place so each land cell (INF) contains the distance
        to its nearest treasure (0). Walls (-1) remain unchanged. If a land
        cell cannot reach any treasure, it should remain INF.

        This method is intentionally left unimplemented for the test harness
        and should raise NotImplementedError.
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        q = deque()
        
        def addCell(r,c)





if __name__ == "__main__":
    main()

