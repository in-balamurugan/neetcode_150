import pytest
from typing import List, Tuple

# PyTest fixture containing the test cases provided by the user
@pytest.fixture(params=[
    # Example 1
    (([1,2,4,2,3,5,3,4], 4), True),
    # Example 2
    (([1,2,3,3,4,5,6,7], 4), False),
])
def case(request) -> Tuple[Tuple[List[int], int], bool]:
    return request.param


def test_is_n_straight_hand(case):
    (hand, groupSize), expected = case
    sol = Solution()
    assert sol.isNStraightHand(hand, groupSize) == expected


# The Solution class must be defined at the bottom of the file.
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for num in hand:
            start = num
            while count[start-1]:
                start -= 1
            
            while 
