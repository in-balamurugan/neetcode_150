import pytest
from typing import List


@pytest.fixture(params=[
    # Example 1
    {
        "input": {
            "n": 4,
            "flights": [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]],
            "src": 0,
            "dst": 3,
            "k": 1,
        },
        "expected": 500,
    },
    # Example 2
    {
        "input": {
            "n": 3,
            "flights": [[1, 0, 100], [1, 2, 200], [0, 2, 100]],
            "src": 1,
            "dst": 2,
            "k": 1,
        },
        "expected": 200,
    },
])
def case(request):
    """Fixture that yields input/expected pairs for the tests."""
    return request.param


def test_find_cheapest_price(case):
    inp = case["input"]
    expected = case["expected"]

    sol = Solution()
    result = sol.findCheapestPrice(
        inp["n"], inp["flights"], inp["src"], inp["dst"], inp["k"]
    )
    assert result == expected


# main function to run the first example
def main():
    example_n = 4
    example_flights = [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]]
    example_src = 0
    example_dst = 3
    example_k = 1

    sol = Solution()
    print(sol.findCheapestPrice(example_n, example_flights, example_src, example_dst, example_k))


# Solution class should be defined at the bottom of the file.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Return the cheapest price from src to dst with at most k stops.

        This method is intentionally unimplemented for the test scaffold.
        """
        prices =[float("inf")]*n
        prices[src] = 0

        for i in range(k+1):
            tmpPrices = prices.copy()

            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
                
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]
        



if __name__ == "__main__":
    main()

