import pytest

@pytest.fixture(params=[
    # (input, expected)
    ([1, 2, 3], 2),             # Example 1
    ([1, 2, 1, 2, 1, 1, 1], 4)  # Example 2
])
def case(request):
    cost, expected = request.param
    return cost, expected

def test_min_cost_climbing_stairs(case):
    cost, expected = case
    sol = Solution()
    assert sol.minCostClimbingStairs(cost) == expected

# Single Solution class must be defined at the bottom of the file
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        Return the minimum cost to reach the top of the staircase.

        NOTE: This method is intentionally left unimplemented for the test scaffold.
        """
        n=len(cost)
        dp= [0] * (n+1)
        
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])
        
        return min(cost[0],cost[1])
            
