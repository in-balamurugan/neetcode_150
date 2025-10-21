import pytest

def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print("Example run:")
    print("Input:", nums, "Target:", target)
    sol = Solution()
    try:
        result = sol.search(nums, target)
        print("Output:", result)
    except NotImplementedError:
        print("search() method not yet implemented.")

@pytest.fixture(params=[
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
])
def test_data(request):
    return request.param

def test_search(test_data):
    (nums, target), expected = test_data
    sol = Solution()
    try:
        result = sol.search(nums, target)
    except NotImplementedError:
        pytest.skip("search() method not yet implemented")
    assert result == expected

class Solution:



    def search(self, nums, target):
        from bisect import bisect_left
        index = bisect_left(nums,target)

        return index if index<len(nums) and nums[index] == target else -1

    
if __name__ == "__main__":
    main()

