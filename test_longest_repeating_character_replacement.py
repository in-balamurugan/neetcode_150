# test_longest_repeating_character_replacement.py
import pytest
from typing import List, Tuple

def main():
    # First example from the prompt
    s = "XYYX"
    k = 2
    try:
        result = Solution().characterReplacement(s, k)  # Solution defined below (method intentionally unimplemented)
        print("Longest repeating character replacement (example 1):", result)
    except NotImplementedError:
        print("characterReplacement is not implemented yet (main ran the first example).")

# PyTest fixture holding exactly the given (input, expected) pairs
@pytest.fixture(params=[
    (("XYYX", 2), 4),
    (("AAABABB", 1), 5)
])
def case(request) -> Tuple[Tuple[str, int], int]:
    return request.param

def test_character_replacement(case):
    (s, k), expected = case
    sol = Solution()
    assert sol.characterReplacement(s, k) == expected

# Solution class must be defined at the bottom with the target method unimplemented
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Return the length of the longest substring which contains only one distinct character
        after performing at most k replacements.

        This method is intentionally left unimplemented for the exercise and should raise
        NotImplementedError until implemented by the user.
        """
        breakpoint()
        count ={}
        res = 0

        l= 0

        maxf =0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf,count[s[r]])

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res =max(res, r-l+1)
        
        return res

# Call main at bottom as requested
if __name__ == "__main__":
    main()

