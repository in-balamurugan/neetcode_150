import pytest
from typing import List, Tuple

# main function runs the first example (will call Solution.combinationSum2, which is intentionally unimplemented)
def main():
    print("Running example from problem statement (Combination Sum II):")
    example_nums = [10,1,2,7,6,1,5]
    example_target = 8
    try:
        print(Solution().combinationSum2(example_nums, example_target))
    except NotImplementedError:
        print("Solution.combinationSum2 is not implemented yet.")


# PyTest fixture holding the provided (input, expected) pairs
@pytest.fixture(params=[
    # ( (nums, target), expected )
    (([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]]),
    (([2,5,2,1,2], 5), [[1,2,2],[5]]),
])
def case(request) -> Tuple[Tuple[List[int], int], List[List[int]]]:
    return request.param


# Single test function that uses the fixture to test the target method
def test_combination_sum2(case):
    (nums, target), expected = case
    sol = Solution()
    result = sol.combinationSum2(nums, target)

    # Compare as sets of tuples because the order of combinations and order within
    # each combination is not important for this problem's correctness.
    assert set(map(tuple, map(sorted, result))) == set(map(tuple, map(sorted, expected)))


# --------------------
# Solution class (must exist at the bottom of the file)
# The target method is intentionally unimplemented.
# --------------------
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        """Return unique combinations where each number may be used at most once.

        This method is left intentionally unimplemented for the test scaffold and
        should raise NotImplementedError until a concrete implementation is provided.
        """
        res =[]
        nums.sort()
        

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return

            if i>=len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i+1,cur,total+nums[i])
            cur.pop()

            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur,total)

        dfs(0,[],0)
        return res


if __name__ == "__main__":
    main()

