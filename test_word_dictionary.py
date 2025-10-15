# test_word_dictionary.py
import pytest


def test_example_case():
    # Example from prompt:
    # Operations:
    # ["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may",
    #  "search", "say", "search", "day", "search", ".ay", "search", "b.."]
    # Expected outputs: [null, null, null, null, false, true, true, true]

#    with pytest.raises(NotImplementedError):
        wd = Solution().WordDictionary()
        wd.addWord("day")
        wd.addWord("bay")
        wd.addWord("may")
#        assert wd.search("say") is False
#        assert wd.search("day") is True
#        assert wd.search(".ay") is True
        assert wd.search("b.") is True


class Solution:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = False


    class WordDictionary:
        def __init__(self):
            self.root = Solution().TrieNode()
            self.word = False

        def addWord(self, word: str) -> None:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Solution().TrieNode()
                cur=cur.children[c]
            cur.word = True

        def search(self, word: str) -> bool:
            
            def dfs(j, root):
                cur = root
                for i in range(j, len(word)):
                    c= word[i]
                    if c == '.':
                        for child in cur.children.values():
                            
                            print(i+1,child)
                            if dfs(i+1, child):
                                return True
                        return False
                    else:
                        if c not in cur.children:
                            return False
                        cur = cur.children[c]

                return cur.word
            return dfs(0,self.root)

