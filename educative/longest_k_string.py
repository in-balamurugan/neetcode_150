"""
PyTest file for "Longest Substring with K Distinct Characters (medium)".
- Contains a single Solution class at the bottom with an unimplemented target method.
- Includes only the provided test cases via a single pytest fixture with params.
- One test function uses the fixture to test the method.
- A main() function runs the first example and is called at the bottom (guarded by __name__ check).
"""

import pytest


# --------------------
# Tests
# --------------------

@pytest.fixture(params=[
    ("araaci", 2, 4),  # Example 1
    ("araaci", 1, 2),  # Example 2
    ("cbbebi", 3, 5),  # Example 3
])
def examples(request):
    """Return (s, k, expected_len) tuples for all provided examples."""
    return request.param


def test_longest_substring_with_k_distinct_examples(examples):
    s, k, expected = examples
    sol = Solution()
    got = sol.longest_substring_with_k_distinct(s, k)
    assert got == expected


# --------------------
# Main (runs first example)
# --------------------

def main():
    s, k, expected = "araaci", 2, 4
    print(f"Input: String=\"{s}\", K={k}")
    try:
        result = Solution().longest_substring_with_k_distinct(s, k)
        print(f"Output: {result} (expected {expected})")
    except NotImplementedError:
        print("The method 'longest_substring_with_k_distinct' is not implemented yet. "
              "Implement it in the Solution class to run this example.")


# --------------------
# Solution (unimplemented)
# --------------------

class Solution:
    def longest_substring_with_k_distinct(self, s: str, k: int) -> int:
        """Return the length of the longest substring with no more than k distinct characters.

        Implement this method.
        """
        
        l=0
        max_length=0
        freq ={}

        for r in range(len(s)):

            #add the char
            right_char=s[r]
            if right_char not in freq:
                freq[right_char]=0
            freq[right_char] += 1
            
            while len(freq)>k:
                left_char = s[l]
                freq[left_char]-= 1
                if freq[left_char] == 0:
                    del freq[left_char]

                l += 1

            max_length = max(max_length,r-l+1)

        return max_length



            #shrink the window










if __name__ == "__main__":
    main()

