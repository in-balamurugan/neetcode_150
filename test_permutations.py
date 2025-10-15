# test_permutations.py
from typing import List, Tuple
import pytest

# --- tests ---------------------------------------------------------------

@pytest.fixture(params=[
    # Example 1
    ([1, 2, 3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    # Example 2
    ([0, 1], [[0,1],[1,0]]),
    # Example 3
    ([1], [[1]]),
])
def case(request) -> Tuple[List[int], List[List[int]]]:
    """Fixture providing (input, expected) pairs."""
    return request.param

def _normalize_permutations(perms: List[List[int]]) -> List[Tuple[int, ...]]:
    """Helper to convert list-of-lists into a sorted list of tuples for comparison."""
    return sorted(tuple(p) for p in perms)

def test_permute(case):
    nums, expected = case
    sol = Solution()
    result = sol.permute(nums)
    assert _normalize_permutations(result) == _normalize_permutations(expected)


# --- main (runs the first example when executed as a script) -------------

def main() -> None:
    """Run the first example and print the result (used when executed as a script)."""
    nums = [1, 2, 3]
    print("Input:", nums)
    sol = Solution()
    print("Output:", sol.permute(nums))


# --- solution (left unimplemented as requested) ---------------------------

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible permutations of nums.
        (Intentionally unimplemented for the testing task.)
        """
        
        res =[]

        def dfs(i):

            if i == len(nums):
                res.append(nums.copy())
                return

            for j in range(i, len(nums)):
                nums[i],nums[j] = nums[j],nums[i]
                dfs(i+1)
                nums[i],nums[j] = nums[j],nums[i]
        dfs(0)
        return res

if __name__ == "__main__":
    main()

