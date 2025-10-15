# insert_interval_test.py
import pytest
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert newInterval into a list of non-overlapping intervals sorted by start,
        and merge if necessary.

        Example 1:
        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output: [[1,6]]

        Example 2:
        Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
        Output: [[1,2],[3,5],[6,7],[9,10]]
        """
        res = []
        for i in range(len(intervals)):
            #not touched
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]:
                    res.append(intervals[i])

            else:
                newInterval= [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "intervals, new_interval, expected",
    [
        # Example 1
        ([[1,3],[4,6]], [2,5], [[1,6]]),
        # Example 2
        ([[1,2],[3,5],[9,10]], [6,7], [[1,2],[3,5],[6,7],[9,10]]),
    ],
)
def test_insert_examples(solver, intervals, new_interval, expected):
    assert solver.insert([list(i) for i in intervals], list(new_interval)) == [list(i) for i in expected]


# Allow running directly: python insert_interval_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

