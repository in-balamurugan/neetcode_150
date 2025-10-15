from typing import List
import pytest

# Example test cases from the prompt
TEST_CASES = [
    (
        ["mobile","mouse","moneypot","monitor","mousepad"],
        "mouse",
        [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
    ),
    (
        ["havana"],
        "havana",
        [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
    )
]

@pytest.fixture(params=TEST_CASES)
def case(request):
    """Fixture that yields (products, searchWord, expected) tuples."""
    return request.param


def test_suggested_products(case):
    products, searchWord, expected = case
    assert Solution().suggestedProducts(products, searchWord) == expected


# A small main function that attempts to run the first example.
# It will catch NotImplementedError from the unimplemented target method.
def main():
    products, searchWord, _ = TEST_CASES[0]
    try:
        result = Solution().suggestedProducts(products, searchWord)
        print("Result:", result)
    except NotImplementedError:
        print("suggestedProducts is not implemented yet.")


class Trie:
    def __init__(self):
        self.eow = False
        self.childs = {}
        self.words = []


# --- Solution placeholder ---
class Solution:





# Call main when the module is executed directly
if __name__ == "__main__":
    main()

