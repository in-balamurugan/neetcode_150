import pytest
from typing import List, Tuple
from collections import deque

@pytest.fixture(params=[
    # (nums, k, expected)
    ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6]),
])
def case(request) -> Tuple[List[int], int, List[int]]:
    return request.param


def test_max_sliding_window(case):
    nums, k, expected = case
    sol = Solution()
    assert sol.maxSlidingWindow(nums, k) == expected


# Solution class must appear at the bottom of the file and the target method
# must be unimplemented (raise NotImplementedError).
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """Return a list containing the maximum element in each sliding window of size k.

        This method is intentionally unimplemented for the exercise and should
        raise NotImplementedError.
        """
        l=r=0
        q = deque()
        output = []

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


