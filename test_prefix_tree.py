# test_prefix_tree.py
import pytest


def test_example_case():
    # Example 1 from prompt:
    # Input:
    # ["Trie", "insert", "dog", "search", "dog", "search", "do",
    #  "startsWith", "do", "insert", "do", "search", "do"]
    #
    # Output:
    # [null, null, true, false, true, null, true]


    #with pytest.raises(NotImplementedError):
        prefixTree = PrefixTree()
        prefixTree.insert("dog")
        assert prefixTree.search("dog") is True
        assert prefixTree.search("do") is False
        assert prefixTree.startsWith("do") is True
        prefixTree.insert("do")
        assert prefixTree.search("do") is True


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word=False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
            
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.end_of_word=True
            

    def search(self, word: str) -> bool:
        cur=self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur =cur.children[c]

        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
