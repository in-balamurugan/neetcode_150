import pytest
from typing import List, Tuple

# PyTest fixture containing the test cases provided by the user
@pytest.fixture(params=[
    # Example 1
    (([1, 2, 3, 4], [2, 2, 4, 1]), 3),
    # Example 2
    (([1, 2, 3], [2, 3, 2]), -1),
])
def case(request) -> Tuple[Tuple[List[int], List[int]], int]:
    return request.param


def test_can_complete_circuit(case):
    (gas, cost), expected = case
    sol = Solution()
    assert sol.canCompleteCircuit(gas, cost) == expected

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1

        return res
