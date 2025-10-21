import pytest
from typing import List, Tuple

# Fixture holding the provided test cases (input, expected)
@pytest.fixture(params=[
    # Example 1
    ( [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True ),
    # Example 2
    ( [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False ),
])
def case(request) -> Tuple[List[List[int]], int, bool]:
    return request.param


def test_target(case):
    matrix, target, expected = case
    sol = Solution()
    assert sol.target(matrix, target) == expected


# A main function that runs the first example. This is placed before the Solution
# class as requested. It will attempt to call the unimplemented method and will
# print a friendly message if the method is not yet implemented.

def main():
    example_matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    example_target = 3
    print("Running first example:")
    print(f"matrix = {example_matrix}")
    print(f"target = {example_target}")
    try:
        result = Solution().target(example_matrix, example_target)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.target is not implemented yet.")


# Solution class must be defined at the bottom of the file. The target method is
# intentionally left unimplemented to match the requirements.
class Solution:
    def target(self, matrix: List[List[int]], target: int) -> bool:
        """Return True if target is in matrix, otherwise False.

        Time complexity required: O(log(m * n)).
        Currently unimplemented.
        """
        
        ROWS,COLS = len(matrix), len(matrix[0])
        l,r = 0, ROWS*COLS-1

        while l<=r:
            m=l+(r-l)//2
            row,col = m // COLS,  m % COLS

            if target  > matrix[row][col]:
                l = m + 1

            elif target < matrix[row][col]:
                r = m-1

            else:
                return True

            
        return False 


if __name__ == "__main__":
    main()

