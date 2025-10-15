import copy
import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    (
        [
            [2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647],
        ],
        [
            [3, -1, 0, 1],
            [2, 2, 1, -1],
            [1, -1, 2, -1],
            [0, -1, 3, 4],
        ],
    ),
    (
        [[-1]],
        [[-1]],
    ),
])
def cases(request) -> Tuple[List[List[int]], List[List[int]]]:
    """Fixture that yields (input_rooms, expected) pairs.

    A deep copy of the input is provided so tests can mutate it.
    """
    rooms, expected = request.param
    return copy.deepcopy(rooms), expected


def test_walls_and_gates(cases):
    rooms, expected = cases
    sol = Solution()
    # The target method is expected to modify rooms in-place.
    sol.wallsAndGates(rooms)
    assert rooms == expected


# A small main to run the first example. Placed before Solution as requested.
def main():
    example_rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    print("Before:")
    for row in example_rooms:
        print(row)
    try:
        Solution().wallsAndGates(example_rooms)
    except NotImplementedError:
        print("wallsAndGates is not yet implemented")
    print("After:")
    for row in example_rooms:
        print(row)


class Solution:
    # Target method (unimplemented on purpose)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """Fill each empty room with the distance to its nearest gate.

        This method is intentionally left unimplemented for the tests.
        """
        ROWS=len(rooms)
        COLS=len(rooms[0])
        from collections import deque
        q=deque()
        visited=set()

        def addCell(r,c):
            if r< 0 or c<0 or r >= ROWS or c >= COLS or (r,c) in visited or rooms[r][c] == -1:
                return
            visited.add((r,c))
            q.append([r,c])    

        from itertools import product

        for r,c in product(range(ROWS), range(COLS)):
            if rooms[r][c] == 0:
                q.append([r,c])
                visited.add((r,c))

        dist =0        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            dist += 1

if __name__ == "__main__":
    main()

