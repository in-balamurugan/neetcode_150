# merge_intervals_test.py
import pytest
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Example 1:
        Input: intervals = [[1,3],[1,5],[6,7]]
        Output: [[1,5],[6,7]]

        Example 2:
        Input: intervals = [[1,2],[2,3]]
        Output: [[1,3]]
        """
        
        intervals.sort(key = lambda x: x[0])
        output=[intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start<= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
        return output

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Example 1
        ([[1,3],[1,5],[6,7]], [[1,5],[6,7]]),
        # Example 2
        ([[1,2],[2,3]], [[1,3]]),
    ],
)
def test_merge_examples(solver, intervals, expected):
    assert solver.merge([list(i) for i in intervals]) == [list(i) for i in expected]


# Allow running directly: python merge_intervals_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

