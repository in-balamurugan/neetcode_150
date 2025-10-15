# combination_sum_test.py
import pytest
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, 
        return a list of all unique combinations of candidates where the chosen numbers sum to target.

        The same number may be chosen from candidates an unlimited number of times.

        Example:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2,2,3],[7]]
        """
        
        res=[]
        nums.sort() if nums is not None else []

        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i,len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                print(j,cur,total,nums[j])
                dfs(j, cur, total+nums[j])
                cur.pop()

        dfs(0,[],0)
        return res
        


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "candidates, target, expected",
    [
        ([2,3,6,7], 7, [[2,2,3],[7]]),                # basic example
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),      # multiple solutions
        ([2], 1, []),                                 # impossible target
        ([1], 2, [[1,1]]),                            # trivial single candidate
        ([1], 1, [[1]]),                              # exact match
        ([3,4,5], 2, []),                             # all too large
    ],
)
def test_combination_sum_examples(solver, candidates, target, expected):
    result = solver.combinationSum(candidates, target)
    # Order of results and order within each combination may vary
    assert sorted([sorted(comb) for comb in result]) == sorted([sorted(comb) for comb in expected])

def test_combination_sum_invalid_types(solver):
    with pytest.raises(TypeError):
        solver.combinationSum(None, 7)

def test_combination_sum_zero_target(solver):
    # target=0 should return [[]] (empty combination)
    result = solver.combinationSum([2,3], 0)
    assert result == [[]]

