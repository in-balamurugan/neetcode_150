# meeting_rooms_test.py
import pytest
from typing import List

class Solution:
    def can_attend_meetings(self, intervals: List[List[int]]) -> bool:
        """
        Determine if a person can attend all meetings without overlaps.

        Args:
          intervals: list of [start, end] pairs where start < end.

        Returns:
          True if no meetings overlap, False otherwise.

        Example 1:
        Input: intervals = [(0,30),(5,10),(15,20)]
        Output: False
        Explanation:
          (0,30) conflicts with (5,10) and (15,20)

        Example 2:
        Input: intervals = [(5,8),(9,15)]
        Output: True
        """
        intervals.sort()
        prevStart,prevEnd = intervals[0][0],intervals[0][1]

        for start,end in intervals[1:]:
            if start<=prevEnd :
                return False
            else:
                prevEnd = end
        return True


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "intervals, expected",
    [
        # Example 1
        ([[0, 30], [5, 10], [15, 20]], False),
        # Example 2
        ([[5, 8], [9, 15]], True),
    ],
)
def test_can_attend_examples(solver, intervals, expected):
    assert solver.can_attend_meetings([list(i) for i in intervals]) == expected


# Allow running directly: python meeting_rooms_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

