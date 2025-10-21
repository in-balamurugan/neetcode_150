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

    def binary_search(self,l, r, nums,target):
        if l>r:
            return -1

        m = l+(r-l)//2

        if nums[m] == target :
            return m

        if nums[m] < target :
            return self.binary_search(m + 1, r, nums, target)
        else:
            return self.binary_search(l, m - 1, nums, target)


    def search(self, nums, target):
        return self.binary_search(0, len(nums)-1, nums,target)

    
        



if __name__ == "__main__":
    main()

