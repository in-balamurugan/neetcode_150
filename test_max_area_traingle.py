import pytest
from typing import List, Optional


@pytest.fixture(params=[
    # Example 1 from problem
    ([[1,1],[1,2],[3,2],[3,3]], 2),
    # Example 2 from problem (collinear -> no axis-parallel triangle)
    ([[1,1],[2,2],[3,3]], -1),
])
def cases(request):
    return request.param


def test_find_max_area_of_triangle(cases):
    coords, expected = cases
    assert Solution().findMaxArea(coords) == expected


def main():
    example = [[1,1],[1,2],[3,2],[3,3]]
    print(f"Running example: coords = {example}")
    try:
        result = Solution().findMaxArea(example)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.findMaxArea is not implemented yet.")


class Solution:
    def findMaxArea(self, coords: List[List[int]]) -> int:
        """Return twice the maximum area of a triangle with at least one side axis-parallel, or -1 if none.
        Not implemented.
        """
        raise NotImplementedError


if __name__ == "__main__":
    main()

