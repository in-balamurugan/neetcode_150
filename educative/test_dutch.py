"""
Dutch National Flag problem (0s, 1s, 2s).

Requirements implemented in this file:
- A single `Solution` class is defined at the bottom of the file.
- The target method exists but is unimplemented (raises NotImplementedError).
- Only the provided test cases are included, using one pytest fixture with params.
- One test function uses the fixture to test the method.
- A `main` function (defined before the Solution class) runs the first example,
  and it is called at the bottom of the file.
"""

import pytest


def main():
    """Run the first example from the prompt."""
    arr = [1, 0, 2, 1, 0]
    print("Input:", [1, 0, 2, 1, 0])
    s = Solution()
    try:
        s.sort_colors(arr)
        print("Output:", arr)
    except NotImplementedError:
        print("sort_colors is not implemented yet")


# ---------------------- PyTest setup ----------------------

@pytest.fixture(
    params=[
        ([1, 0, 2, 1, 0], [0, 0, 1, 1, 2]),
        ([2, 2, 0, 1, 2, 0], [0, 0, 1, 2, 2, 2]),
    ]
)
def cases(request):
    """Provides (input_array, expected_array) pairs."""
    # Copy input to avoid accidental mutation across tests
    arr_in, expected = request.param
    return (list(arr_in), expected)


def test_sort_colors_in_place(cases):
    """Tests that the method sorts in place to match the expected output."""
    arr, expected = cases
    s = Solution()
    s.sort_colors(arr)
    assert arr == expected


# ---------------------- Solution (at bottom) ----------------------

class Solution:
    def sort_colors(self, nums):
        """
        Sort the array containing only 0s, 1s, and 2s in-place.

        Expected behavior (for when implemented):
        - Modify `nums` in-place to be sorted non-decreasingly.
        - Do not return anything.

        This method is intentionally unimplemented.
        """
        from collections import Counter
        c=dict(Counter(nums))

        res=[]
        c=dict(sorted(c.items()))

        i=0
        for key,item in c.items():

            for _ in range(item):
                nums[i] =(key)
                i += 1


if __name__ == "__main__":
    main()

