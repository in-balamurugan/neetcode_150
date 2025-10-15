from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self,strs):
        
        
        
        str_list=defaultdict(list)
        str_map=defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                i = ord(c) - ord('a')
                key[i]=1
            str_map[tuple(key)].append(s)


        return list(str_map.values())




def test_group_anagrams():
    s = Solution()

    assert {frozenset(g) for g in s.group_anagrams(["act","pots","tops","cat","stop","hat"])} == {
        frozenset(["hat"]),
        frozenset(["act", "cat"]),
        frozenset(["stop", "pots", "tops"]),
    }

    assert {frozenset(g) for g in s.group_anagrams(["x"])} == {
        frozenset(["x"])
    }

    assert {frozenset(g) for g in s.group_anagrams([""])} == {
        frozenset([""])
    }

        
