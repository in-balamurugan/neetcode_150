import pytest
from typing import List, Tuple

# main function runs the first example (will call Solution.subsets, which is intentionally unimplemented)
def main():
    print("Running example from problem statement:")
    example = [1, 2, 3]
    try:
        print(Solution().subsets(example))
    except NotImplementedError:
        print("Solution.subsets is not implemented yet.")


# PyTest fixture holding the provided (input, expected) pairs
@pytest.fixture(params=[
    # (input, expected)
    ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ([0], [[], [0]]),
])
def case(request) -> Tuple[List[int], List[List[int]]]:
    return request.param


# Single test function that uses the fixture to test the target method
def test_subsets(case):
    nums, expected = case
    sol = Solution()
    result = sol.subsets(nums)

    # Compare as sets of tuples because the order of subsets or the order of sets in the result
    # is not important per the problem statement.
    assert set(map(tuple, result)) == set(map(tuple, expected))


# --------------------
# Solution class (must exist at the bottom of the file)
# The target method is intentionally unimplemented.
# --------------------
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """Return all possible subsets (the power set) of unique elements in nums.

        This method is left intentionally unimplemented for the test scaffold and
        """
        res=[]
        subset=[]

        def dfs(i):

            if i>= len(nums):
                res.append(subset.copy())
                print("returning",subset)
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)


        dfs(0)
        return res



if __name__ == "__main__":
    main()

