"""
Fruits into Baskets (medium)

Problem Statement:
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put the maximum number of fruits in both baskets. Each basket can have only one type of fruit. You must pick consecutively from trees without skipping, and you stop when a third fruit type would be needed.

Example 1:
Input:  Fruit = ['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: Pick from subarray ['C', 'A', 'C'] -> 2 'C' and 1 'A'.

Example 2:
Input:  Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: Pick from subarray ['B', 'C', 'B', 'B', 'C'] -> 3 'B' and 2 'C'.
"""

import pytest


# --------------------------- PyTest setup ---------------------------

@pytest.fixture(
    params=[
        (['A', 'B', 'C', 'A', 'C'], 3),
        (['A', 'B', 'C', 'B', 'B', 'C'], 5),
    ]
)
def fruit_cases(request):
    """
    Parametrized fixture yielding (input, expected) pairs.
    """
    return request.param


def test_total_fruit(fruit_cases):
    """
    Single test that uses the fixture to validate the target method.
    """
    fruits, expected = fruit_cases
    sol = Solution()
    assert sol.total_fruit(fruits) == expected


# --------------------------- Main runner ---------------------------

def main():
    """
    Run the first example.
    """
    fruits = ['A', 'B', 'C', 'A', 'C']
    print("Example 1 input:", fruits)
    try:
        result = Solution().total_fruit(fruits)
        print("Example 1 output:", result)
    except NotImplementedError:
        print("Solution.total_fruit is not yet implemented.")


class Solution:
    def total_fruit(self, fruits):
        """
        Return the maximum number of fruits that can be picked into two baskets
        from a contiguous subarray of `fruits`, where each basket can only
        contain one fruit type.

        :param fruits: List[str] representing fruit types per tree.
        :return: int
        """
        
        l=0
        max_length=0
        freq={}


        for r in range(len(fruits)):
            
            right_fruit = fruits[r]
            if r not in freq:
                freq[right_fruit] = 0
            freq[right_fruit] += 1

            while len(freq)>2:
                left_fruit = fruits[l]
                freq[left_fruit] -= 1

                if freq[left_fruit] == 0:
                    del freq[left_fruit]
                l += 1



            max_length=max(max_length, r-l+1)
        return max_length

if __name__ == "__main__":
    main()
