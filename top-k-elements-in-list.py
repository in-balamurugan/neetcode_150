#Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def top_k_frequent(self,nums: List[int], k):
        #create dict
        nums_dict=defaultdict(int)
        for num in nums:
            nums_dict[num] += 1

        #create min heap
        nums_heap=[]
        for num in nums_dict:
            heapq.heappush(nums_heap,(nums_dict[num],num))

            if len(nums_heap)>k:
                heapq.heappop(nums_heap)

        #create list
        nums_list=[]
        for _ in range(k):
            nums_list.append(heapq.heappop(nums_heap)[1])

        return nums_list

def test_top_k_elements_in_list():

    s = Solution()

    # Example 1
    result = s.top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    expected = [1, 2]
    assert set(result) == set(expected)
    assert len(result) == len(expected)

    # Example 2
    result = s.top_k_frequent([1], 1)
    expected = [1]
    assert set(result) == set(expected)
    assert len(result) == len(expected)

    # Example 3
    result = s.top_k_frequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2)
    expected = [1, 2]
    assert set(result) == set(expected)
    assert len(result) == len(expected)
    
