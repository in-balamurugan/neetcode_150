# meeting_rooms_ii_test.py
import pytest
from typing import List
import heapq

class Solution:
    def min_days(self, intervals: List[List[int]]) -> int:
        """
        Given an array of meeting time intervals [start, end] with start < end,
        return the minimum number of days required to schedule all meetings
        without conflicts.

        Note: intervals that touch (end == start) do not conflict.

        Example 1:
        Input: intervals = [(0,40),(5,10),(15,20)]
        Output: 2
        Explanation:
          day1: (0,40)
          day2: (5,10),(15,20)

        Example 2:
        Input: intervals = [(4,9)]
        Output: 1
        """


        intervals.sort(key = lambda x: x[0])
        min_heap=[]
        
        for interval in intervals:
            
            if min_heap and min_heap[0]<=interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,interval[1])

        return len(min_heap)


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Example 1
        ([[0, 40], [5, 10], [15, 20]], 2),
        # Example 2
        ([[4, 9]], 1),
    ],
)
def test_min_days_examples(solver, intervals, expected):
    assert solver.min_days([list(i) for i in intervals]) == expected


# Allow running directly: python meeting_rooms_ii_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

