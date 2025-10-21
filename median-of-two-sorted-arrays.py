import pytest
from typing import List, Tuple

# Main function that "runs" the first example.
# It will attempt to call the Solution method but will catch the NotImplementedError
# because the method is intentionally left unimplemented per instructions.
def main() -> None:
    nums1 = [1, 2]
    nums2 = [3]
    expected = 2.0
    print("Running first example:")
    print(f" nums1 = {nums1}")
    print(f" nums2 = {nums2}")
    print(f" expected median = {expected}")
    try:
        result = Solution().findMedianSortedArrays(nums1, nums2)
        print(f" Solution returned: {result}")
    except NotImplementedError:
        print(" Solution.findMedianSortedArrays is not implemented (expected).")


# --- PyTest tests ---
# Use a single fixture with params to hold the provided input/expected pairs.
@pytest.fixture(params=[
    # Example 1
    (((1, 2), (3,)), 2.0),
    # Example 2
    (((1, 3), (2, 4)), 2.5),
])
def case(request) -> Tuple[Tuple[List[int], List[int]], float]:
    (nums1_tuple, nums2_tuple), expected = request.param
    # convert tuples to lists for the test
    nums1 = list(nums1_tuple)
    nums2 = list(nums2_tuple)
    return (nums1, nums2), expected


def test_find_median_sorted_arrays(case):
    (nums1, nums2), expected = case
    sol = Solution()
    assert sol.findMedianSortedArrays(nums1, nums2) == expected


# --- Solution class (must be at the bottom) ---
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays in O(log(m+n)) time.
        Intentionally left unimplemented as required by the instructions.
        """
        
        #Brute force
        merged = nums1 + nums2
        merged.sort()

        totalLen = len(merged)
        if totalLen % 2 == 0:
            return (merged[totalLen // 2 - 1] + merged[totalLen // 2]) / 2.0
        else:
            return merged[totalLen // 2]

if __name__ == "__main__":
    main()

