# longest_substring_test.py
import pytest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Implement this function.

        Given a string s, find the length of the longest substring without repeating characters.
        """
        char_set = set()
        l= 0 
        res=0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                print(f'removed {s[l]=}, {l=}')
            char_set.add(s[r])
            res=max(res,r-l+1)
            
            print(f'{l=},{r=},{char_set=}')
        return res



# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),  # Example 1
        ("bbbbb", 1),     # Example 2
        ("pwwkew", 3),    # Example 3
    ],
)
def test_length_of_longest_substring(solver, s, expected):
    assert solver.lengthOfLongestSubstring(s) == expected


# Allow running directly: python longest_substring_test.py
if __name__ == "__main__":
    import sys
    import pytest as _pytest
    sys.exit(_pytest.main(["-vvs", __file__]))

