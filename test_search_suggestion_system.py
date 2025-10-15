import pytest
from typing import List


@pytest.fixture(params=[
    # Example 1 from problem
    ((["mobile","mouse","moneypot","monitor","mousepad"], "mouse"),
     [["mobile","moneypot","monitor"], ["mobile","moneypot","monitor"], ["mouse","mousepad"], ["mouse","mousepad"], ["mouse","mousepad"]]),
])
def cases(request):
    return request.param


def test_suggested_products(cases):
    (products, searchWord), expected = cases
    assert Solution().suggestedProducts(products, searchWord) == expected


def main():
    example_products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    example_search = "mouse"
    print(f"Running example: products = {example_products}, searchWord = '{example_search}'")
    try:
        result = Solution().suggestedProducts(example_products, example_search)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.suggestedProducts is not implemented yet.")


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Return a list of lists of suggested products for each prefix of searchWord. (Not implemented)"""
        raise NotImplementedError


if __name__ == "__main__":
    main()

