# test_koko_eating.py
import pytest
from typing import List

def main():
    # Run the first example (will raise NotImplementedError because solution is unimplemented)
    piles = [1, 4, 3, 2]
    h = 9
    print("Example 1 result:", Solution().minEatingSpeed(piles, h))


@pytest.fixture(params=[
    # Each item is ((piles, h), expected)
    (([1, 4, 3, 2], 9), 2),
    (([25, 10, 23, 4], 4), 25),
])
def case(request):
    return request.param


def test_min_eating_speed(case):
    (piles, h), expected = case
    sol = Solution()
    assert sol.minEatingSpeed(piles, h) == expected


# Solution class must be defined at the bottom of the file
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Find the minimum integer k such that all piles can be eaten within h hours.
        Method intentionally left unimplemented for the test scaffold.
        """
        l,r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            
            totalTime = 0

            for p in piles:
                import math
                totalTime += math.ceil(p / k)
            if totalTime <=h :
                res = k
                r= k-1
            else:
                l=k+1
        return res
        

if __name__ == "__main__":
    main()

