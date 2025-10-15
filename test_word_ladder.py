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
    with pytest.raises(NotImplementedError):
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
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        n = len(wordList)
        m = len(wordList[0])
        
        adj =[[] for _ in range(n)]
        
        mp ={}

        for i in range(n):
            mp[wrodList[i]] ==  i


        for i in range(n):
            for j in range(i+1,n):
                
                cnt =0
                for k in range(n):
                    if wordList[i][k] != wordList[j][k]:

                        cnt += 1

                    if cnt==1:
                        adj[i].append(j)
                        adj[j].append(i)


        q,res = deque(),1
        visit =set()

        for i in range(m):
            for c in range(97,123):

                if chr(c) == beginWord[i]:
                    continue

                word = beginWord[:i] + chr(c) + beginWord[i+1:]
                
                if word in mp and mp[word] not in visit:

                    q.append(word)
                    visit.add(mp[word])
                
                while q:
                    res += 1

                    for i in range(len(q)):
                        node=q.popleft()

                        if wordList


















                








# Call main if run as a script
if __name__ == "__main__":
    main()
est_word_ladder.py
