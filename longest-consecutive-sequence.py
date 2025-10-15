#Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
#A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
#You must write an algorithm that runs in O(n) time.

from typing import List



class Solution:
    def longest_consecutive_sequence(self,l:List[int]) -> int:
        s=set(l)

        if not l:
            return 0
        max_len=1
        for i  in s:
            if i-1 not in s:

                h=i
                count_len=1
                while h+1 in s:
                    h += 1
                    count_len += 1
                max_len = max(max_len,count_len)
        return max_len



if __name__ == '__main__':
    s = Solution()
    
    assert s.longest_consecutive_sequence([2,20,4,10,3,4,5]) == 4
    assert s.longest_consecutive_sequence([0,3,2,5,4,6,1,1]) == 7
