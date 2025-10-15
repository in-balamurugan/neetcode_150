import pytest

@pytest.fixture(params=[
    # (numbers, target, expected)
    ([1, 2, 3, 4], 3, [1, 2]),
])
def case(request):
    return request.param


def test_two_sum(case):
    numbers, target, expected = case
    sol = Solution()
    assert sol.twoSum(numbers, target) == expected


class Solution:
    def twoSum(self, numbers, target):
        
        l,r =0 , len(numbers)-1

        while l<r:

            curSum =numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1

            elif curSum < target:
                l +=1

            else:
                return [l+1,r+1]
            
        return []

