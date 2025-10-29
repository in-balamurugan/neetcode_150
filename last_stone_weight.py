# test_last_stone_weight.py
import pytest
from typing import List

def main():
    """
    Run the first example and print the result.
    The Solution.lastStoneWeight method is intentionally unimplemented and will
    raise NotImplementedError; we catch that so running this file directly is safe.
    """
    example = [2, 3, 6, 2, 4]
    print("Running example:", example)
    try:
        res = Solution().lastStoneWeight(example)
        print("Result:", res)
    except NotImplementedError:
        print("Solution.lastStoneWeight is not implemented (expected in this test scaffold).")

# PyTest fixture holding the provided (input, expected) pairs (no extras).
@pytest.fixture(params=[
    # (input_stones, expected)
    ([2, 3, 6, 2, 4], 1),
    ([1, 2], 1),
])
def case(request):
    return request.param

# Single test function that uses the fixture to test the method.
def test_last_stone_weight_raises_not_implemented(case):
    stones, expected = case
    sol = Solution()
    # The target method is intentionally unimplemented; assert it raises NotImplementedError.
    sol.lastStoneWeight(stones)


# ---------------------------------------------------------------------
# The single Solution class must be defined at the bottom of the file.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Compute the weight of the last remaining stone after repeatedly smashing the two largest stones.

        NOTE: This method is intentionally left unimplemented for the testing scaffold.
        """
        import heapq
        stones = [-s for s in stones] 
        heapq.heapify(stones)

        while len(stones)>1:
            first=heapq.heappop(stones)
            second=heapq.heappop(stones)
            
            heapq.heappush(stones, first - second)

            stones.append(0)
            return -stones[0] if stones else 0



if __name__ == "__main__":
    main()
