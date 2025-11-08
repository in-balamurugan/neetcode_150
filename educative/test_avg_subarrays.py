# test_avg_subarrays.py
import pytest
from typing import List, Tuple

# --- main (runs first example when executed as a script) ---
def main() -> None:
    """
    Demonstrates the first example. This will try to call the unimplemented
    Solution.find_averages method and will print a short message if it's not
    implemented (so importing this file for pytest won't execute the call).
    """
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 5
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]
    print("Example input:", arr, "K =", K)
    print("Expected averages for the first example:", expected)
    try:
        result = Solution().find_averages(arr, K)
        print("Solution output:", result)
    except NotImplementedError:
        print("Solution.find_averages is not implemented yet.")

# --- PyTest fixtures and tests ---
# The fixture below contains (input, expected) pairs.
# Each input is a tuple (arr, K). The expected value is a list of floats.
@pytest.fixture(params=[
    # First example (standard)
    (((1, 3, 2, 6, -1, 4, 1, 8, 2), 5), [2.2, 2.8, 2.4, 3.6, 2.8]),
    # Simple increasing sequence
    (((1, 2, 3, 4, 5), 2), [1.5, 2.5, 3.5, 4.5]),
    # All negatives
    (((-1, -2, -3, -4), 3), [-2.0, -3.0]),
])
def example(request) -> Tuple[Tuple[Tuple[int, ...], int], List[float]]:
    """
    Returns ((arr_tuple, K), expected_list)
    The test function will convert arr_tuple back to a list before calling the method.
    """
    return request.param

def test_find_averages(example):
    (arr_tuple, K), expected = example
    arr = list(arr_tuple)
    result = Solution().find_averages(arr, K)
    # Use pytest.approx for float comparison (element-wise)
    assert result == pytest.approx(expected)

# --- Solution class (must be at the bottom) ---
class Solution:
    def find_averages(self, arr: List[float], K: int) -> List[float]:
        """
        Given an array arr, return a list of averages of all contiguous subarrays
        of size K.

        This method is intentionally left unimplemented for the exercise.
        """
        
        result= []
        start,asum=0,0
        l=len(arr)

        for end in range(l):
            
            asum+=arr[end]
            if end>=K-1:
                result.append(asum/K)
                asum-=arr[start]
                start+=1

        return result



if __name__ == "__main__":
    main()

