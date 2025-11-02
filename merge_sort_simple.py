"""
LeetCode-style problem: Merge Sort (Iterative or Recursive)

Given an integer array nums, implement a function to return a new array containing
all the elements of nums in non-decreasing order (i.e., sorted ascending).

You should implement the function `sortArray(self, nums: List[int]) -> List[int]`
inside the `Solution` class below. **Do not implement the solution here** — the
method is intentionally left unimplemented (it raises NotImplementedError).

This file contains pytest tests (below) that will exercise `Solution.sortArray`.

Constraints (typical LeetCode style):
- 1 <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

"""

from typing import List, Tuple
import pytest

# ---------------------------
# PyTest tests
# ---------------------------

# Only the test cases provided by the user are included (no extras).
# Each entry is a tuple: (input_list, expected_sorted_list)
@pytest.fixture(params=[
    # First (and only) example provided in the conversation
    ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
])
def cases(request) -> Tuple[List[int], List[int]]:
    return request.param


def test_sort_array(cases: Tuple[List[int], List[int]]):
    nums, expected = cases
    sol = Solution()
    assert sol.sortArray(nums) == expected


# ---------------------------
# Main (runs the first example)
# ---------------------------

def main() -> None:
    example = [38, 27, 43, 3, 9, 82, 10]
    print("Example input:", example)
    try:
        out = Solution().sortArray(example)
        print("Output:", out)
    except NotImplementedError:
        print("Solution.sortArray is not implemented.")


# ---------------------------
# Solution class (TO BE IMPLEMENTED BY THE USER)
# ---------------------------

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Sorts and returns a new list containing the elements of nums in
        non-decreasing order. Must be implemented by the user.
        """
        n = len(nums)
        w=1

        res =nums[:]

        def merge(l,r):

            result,i,j =[],0,0

            while i <len(l) and j<len(r):
                if l[i] <= r[j]:
                    result.append(l[i])
                    i+= 1
                else:
                    result.append(r[j])
                    j += 1
            result.extend(l[i:])
            result.extend(r[j:])
            return result

        while w < n:
            for i in range(0, n, 2 * w):
                 left = res[i:i + w]
                 right = res[i + w :i + 2 * w]
                 res[i:i + 2 * w] = merge(left, right)
            w *= 2
        return res

# Call main when run as a script
if __name__ == "__main__":
    main()

