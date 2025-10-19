import pytest


@pytest.fixture(params=[
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [0, 1]),
])
def example_cases(request):
    """Fixture containing input-output pairs for the Two Sum problem."""
    return request.param


def test_two_sum(example_cases):
    """Tests the Solution.twoSum method using the provided fixture."""
    (nums, target), expected = example_cases
    sol = Solution()
    assert sol.twoSum(nums, target) == expected


def main():
    """Runs the first example manually."""
    nums, target = [2, 7, 11, 15], 9
    print("Example input:", nums, "Target:", target)
    sol = Solution()
    try:
        result = sol.twoSum(nums, target)
        print("Output:", result)
    except NotImplementedError:
        print("twoSum method not yet implemented.")


class Solution:
    def twoSum(self, nums, target):
        """Return indices of two numbers such that they add up to target."""
        
        target_dict={}
        for i,num in enumerate(nums):
            if num in target_dict:
                return [target_dict[num],i]
            else:
                target_dict[target-num] =i

if __name__ == "__main__":
    main()

