import pytest
from typing import List, Tuple

@pytest.fixture(params=[
    # (input_matrix, expected_output)
    ([[1, 2], [3, 4]], [1, 2, 4, 3]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
     [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
])
def case(request) -> Tuple[List[List[int]], List[int]]:
    """Fixture supplying (matrix, expected) pairs as requested."""
    return request.param

def test_spiral_order(case):
    matrix, expected = case
    sol = Solution()
    assert sol.spiralOrder(matrix) == expected

# A small main to run the first example (placed before the Solution class).
def main():
    example = [[1, 2], [3, 4]]
    try:
        out = Solution().spiralOrder(example)
        print("Spiral order of", example, "is", out)
    except NotImplementedError:
        print("spiralOrder is not implemented yet (NotImplementedError).")

# Call main at the bottom as requested (this will not raise because main catches the NotImplementedError).

# Single Solution class defined at the bottom of the file.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return elements of `matrix` in spiral order.

        This method is intentionally left unimplemented for the test harness;
        it should raise NotImplementedError to satisfy the requirement.
        """
        m,n = len(matrix), len(matrix[0])
        res =[]

        def dfs(row,col,r,c,dr,dc):
            if row ==0 or col ==0:
                return

            for i in range(col):
                r += dr
                c += dc
                res.append(matrix[r][c])
            
            dfs(col,row-1,r,c,dc,-dr)            

        dfs(m,n,0,-1,0,1)

        return res


main()



