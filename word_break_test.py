# Save as word_break_test.py
# (This comment does not start the filename with "test_". Rename the file to begin with "test_" if you want pytest auto-discovery.)
from typing import List
import pytest
import re

class Solution:
    """
    Solution container for the Word Break problem.

    Implement `wordBreak(self, s: str, wordDict: List[str]) -> bool`
    to return True if `s` can be segmented into a space-separated sequence
    of one or more dictionary words from `wordDict` (words may be reused).
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            s=re.sub(word,"",s)
            print(s)
        return True if s=="" else False

# ---- Tests (only the examples you provided) ----

def test_example_1():
    sol = Solution()
    assert sol.wordBreak("neetcode", ["neet", "code"]) is True

def test_example_2():
    sol = Solution()
    assert sol.wordBreak("applepenapple", ["apple", "pen", "ape"]) is True

def test_example_3():
    sol = Solution()
    assert sol.wordBreak("catsincars", ["cats", "cat", "sin", "in", "car"]) is False

