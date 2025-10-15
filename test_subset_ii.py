import pytest
from typing import List, Tuple

# main function runs the first example (will call Solution.subsetsWithDup, which is intentionally unimplemented)
def main():
    print("Running example from problem statement (Subsets II):")
    example = [1, 2, 2]
    try:
        print(Solution().subsetsWithDup(example))
    except NotImplementedError:
        print("Solution.subsetsWithDup is not implemented yet.")


# PyTest fixture holding the provided (input, expected) pairs
@pytest.fixture(params=[
    # (input, expected)
    ([1, 2, 2], [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]),
    ([0], [[], [0]]),
])
def case(request) -> Tuple[List[int], List[List[int]]]:
    return request.param


# Single test function that uses the fixture to test the target method
def test_subsets_with_dup(case):
    nums, expected = case
    sol = Solution()
    result = sol.subsetsWithDup(nums)

    # Compare as sets of tuples because the order of subsets or the order of sets in the result
    # is not important per the problem statement.
    assert set(map(tuple, result)) == set(map(tuple, expected))


# --------------------
# Solution class (must exist at the bottom of the file)
# The target method is intentionally unimplemented.
# --------------------
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Return all unique subsets of nums (which may contain duplicates).

        This method is left intentionally unimplemented for the test scaffold and
        should raise NotImplementedError until a concrete implementation is provided.
        """
        
        nums.sort()
        res=[]
        subset =[]

        dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return

            for j in range(i,len(nums):
                if j>i and nums[j]==nums[j-1]:
                    continue

            subset.append(j+1)
            subs

        dfs(0)

        return res

if __name__ == "__main__":
    main()

