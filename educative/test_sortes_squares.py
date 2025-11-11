# test_sorted_squares.py
import pytest
from typing import List


def main() -> None:
    """
    Run the first example to show expected I/O shape.
    The Solution.sortedSquares method is intentionally unimplemented
    and will raise NotImplementedError when called.
    """
    nums = [-2, -1, 0, 2, 3]
    expected = [0, 1, 4, 4, 9]
    print("Input:   ", nums)
    print("Expected:", expected)
    try:
        result = Solution().sortedSquares(nums)  # will raise NotImplementedError
        print("Result:  ", result)
    except NotImplementedError as e:
        print("sortedSquares is not implemented yet:", e)


# ---------- Tests ----------

@pytest.fixture(
    params=[
        ([-2, -1, 0, 2, 3], [0, 1, 4, 4, 9]),   # Example 1
        ([-3, -1, 0, 1, 2], [0, 1, 1, 4, 9]),   # Example 2
    ]
)
def case(request):
    """Parametrized (input, expected) pairs from the prompt."""
    return request.param


def test_sorted_squares(case):
    nums, expected = case
    assert Solution().sortedSquares(nums) == expected


# ---------- Solution skeleton (must remain unimplemented) ----------

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given a sorted array of integers (may include negatives),
        return a new array of the squares of each number in non-decreasing order.
        """
        l,r = 0,len(nums)-1
        res= []
        
        while l<=r:
            num_r_square=nums[r]**2
            num_l_square=nums[l]**2

            if num_l_square > num_r_square:
                res.append(num_l_square)
                l += 1
            else:
                res.append(num_r_square)
                r -= 1

        return res[::-1]



if __name__ == "__main__":
    main()

