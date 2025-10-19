import pytest
from typing import List, Tuple


@pytest.fixture(params=[
    ([1, 0, 1, 2], [0, 1, 1, 2]),
    ([2, 1, 0], [0, 1, 2]),
])
def cases(request) -> Tuple[List[int], List[int]]:
    """Fixture that yields (input_list, expected_list) pairs.

    The input_list is copied inside the test to ensure the fixture data
    isn't mutated across tests.
    """
    inp, exp = request.param
    return list(inp), list(exp)


def test_sort_colors(cases):
    nums, expected = cases
    sol = Solution()
    sol.sortColors(nums)
    assert nums == expected


def main():
    # run the first example
    nums = [1, 0, 1, 2]
    print("Before:", nums)
    Solution().sortColors(nums)
    print("After:", nums)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """Sorts nums in-place so that 0s, then 1s, then 2s.

        This method is intentionally left unimplemented for the test file
        — it should raise NotImplementedError until the user provides
        an implementation.
        """
        from collections import Counter
        count= Counter(nums)

        index = 0

        for color in (0,1,2):
            for _ in range(count[color]):
                nums[index]= color
                index += 1

        



if __name__ == "__main__":
    main()

