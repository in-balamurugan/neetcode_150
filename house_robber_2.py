import pytest


@pytest.fixture(params=[
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
])
def cases(request):
    """Fixture yielding (input, expected) pairs for the tests."""
    return request.param


def test_rob(cases):
    nums, expected = cases
    assert Solution().rob(nums) == expected


def main():
    """Run the first example and show the result (or a friendly message if not implemented)."""
    example = [2, 3, 2]
    print(f"Running example: nums = {example}")
    try:
        result = Solution().rob(example)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.rob is not implemented yet.")


class Solution:
    def rob(self, nums: list[int]) -> int:
        """Return the maximum amount that can be robbed (not implemented)."""
    
        def rob_house(house_list):

            rob1 =0
            rob2=0

            for num in house_list:
                temp = max(rob1+num,rob2)
                rob1=rob2
                rob2=temp
            return rob2

        return max(rob_house(nums[1:]) , rob_house(nums[:-1]))




if __name__ == "__main__":
    main()

