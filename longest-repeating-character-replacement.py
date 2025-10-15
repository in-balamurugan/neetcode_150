# character_replacement_test.py
import pytest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Implement this function.

        You are given a string s and an integer k. You can choose any character of
        the string and change it to any other uppercase English character. You can
        perform this operation at most k times.

        Return the length of the longest substring containing the same letter
        you can get after performing the above operations.
        """
        raise NotImplementedError("Implement this method in the Solution class")


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),      # Example 1
        ("AABABBA", 1, 4),   # Example 2
    ],
)
def test_character_replacement_examples(solver, s, k, expected):
    assert solver.

