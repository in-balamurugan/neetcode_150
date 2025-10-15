#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from typing import List
from collections import defaultdict

class Solution:
	def is_anagram(self,s,t):
		
		def convert_map(a):
			b=defaultdict(int)
			for i in a:
				if i in b:
					b[i] += 1
				else:
					b[i]=1
			return b
		t_map = convert_map(t)
		
		s_map = convert_map(s)
		return t_map == s_map		

                         
              

if __name__ == '__main__':
	s = Solution()
	
	assert s.is_anagram(s='racecar',t='carrace') == True
	assert s.is_anagram(s='jar',t='jam') == False
