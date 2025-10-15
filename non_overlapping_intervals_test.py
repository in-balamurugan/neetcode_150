# non_overlapping_intervals_test.py
import pytest
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Given an array of intervals intervals where intervals[i] = [starti, endi],
        return the minimum number of intervals you need to remove to make the rest non-overlapping.

        Example 1:
        Input: intervals = [[1,2],[2,4],[1,4]]
        Output: 1
        Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

        Example 2:
        Input: intervals = [[1,2],[2,4]]
        Output: 0
        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][0]

        for start, end in intervals[i:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = max(end,prevEnd)

        return res

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Example 1
        ([[1,2],[2,4],[1,4]], 1),
        # Example 2
        ([[1,2],[2,4]], 0),
    ],
)
def test_erase_overlap_examples(solver, intervals, expected):
    assert solver.eraseOverlapIntervals([list(i) for i in intervals]) == expected


# Allow running directly: python non_overlapping_intervals_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

