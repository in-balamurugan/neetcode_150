# climbing_stairs_test.py
import pytest

class Solution:

    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        """
        You are given an integer n representing the number of steps to reach 
        the top of a staircase. You can climb with either 1 or 2 steps at a time.

        Return the number of distinct ways to climb to the top of the staircase.

        Constraints:
          1 <= n <= 30
        """
        if n<=2:
            return n

        if n in self.memo:
            return self.memo[n]

        self.memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.memo[n]


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),   # Only one way
        (2, 2),   # (1+1), (2)
        (3, 3),   # (1+1+1), (1+2), (2+1)
        (4, 5),   # Fibonacci growth
        (5, 8),
        (10, 89),
        (30, 1346269),  # upper constraint
    ],
)
def test_climb_stairs(solver, n, expected):
    # When implemented, this should return the expected result
    assert solver.climbStairs(n) == expected


# Allow running directly: python climbing_stairs_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-q", __file__]))

