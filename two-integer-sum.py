from typing import List

class Solution:
	def two_sum(self,nums,target):
		
		prev_map={}
		
		for i,num in enumerate(nums):
		
			if (target-num) in prev_map:
				
				return [prev_map[target-num],i]
				
			else:
				prev_map[num] = i 

if __name__ == '__main__':
	s = Solution()
	
	assert s.two_sum(nums = [3,4,5,6], target = 7) == [0,1]
	assert s.two_sum(nums=[5,5],target =10) == [0,1]
