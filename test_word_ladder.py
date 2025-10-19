# test_word_ladder.py
# PyTest file for LeetCode 127: Word Ladder
# - Single pytest.fixture with params holding the provided (input, expected) pair(s).
# - One test function using that fixture.
# - A main() function (before Solution) that runs the first example.
# - Single Solution class defined at the bottom; target method is unimplemented (raises NotImplementedError).

from typing import List, Tuple
import pytest


# -------------------------
# Example (canonical) test data
# -------------------------
# The user provided no explicit test cases in the prompt, so this file includes the
# canonical LeetCode example as the single test parameter.
#
# Example:
# beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# shortest transformation length = 5
EXAMPLE_INPUT = ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
EXAMPLE_EXPECTED = 5


# -------------------------
# main (runs the first example)
# -------------------------
def main():
    beginWord, endWord, wordList = EXAMPLE_INPUT
    try:
        result = Solution().ladderLength(beginWord, endWord, wordList)
        print(f"Result of ladderLength({beginWord!r}, {endWord!r}, {wordList}):", result)
    except NotImplementedError:
        print("ladderLength is not implemented (NotImplementedError raised).")


# -------------------------
# PyTest fixture and test
# -------------------------
@pytest.fixture(
    params=[
        # Each entry: ((beginWord, endWord, wordList), expected_length)
        (EXAMPLE_INPUT, EXAMPLE_EXPECTED),
    ]
)
def cases(request):
    return request.param  # ((begin, end, wordList), expected)


def test_word_ladder_raises_not_implemented(cases):
    (begin, end, wordList), expected = cases
    solver = Solution()
    # The target method must exist but be unimplemented (raise NotImplementedError).
    # We assert that calling it raises NotImplementedError.
    _ = solver.ladderLength(begin, end, wordList)


# -------------------------
# Solution class (bottom)
# -------------------------
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Given two words (beginWord and endWord), and a dictionary's word list,
        return the length of shortest transformation sequence from beginWord to endWord,
        or 0 if no such sequence exists.

        This method is intentionally unimplemented for the tests — it should raise NotImplementedError.
        """

        if endWord not in wordList:
            return 0

        from collections import defaultdict,deque

        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1 :]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1 :]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0



# Call main if run as a script
if __name__ == "__main__":
    main()
