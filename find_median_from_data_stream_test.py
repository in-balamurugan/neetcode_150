# find_median_from_data_stream_test.py
import pytest
import heapq

class Solution:
    def __init__(self):
        """
        Initialize data structure to support streaming integer insertion and median retrieval.

        Implement addNum and findMedian methods.
        """
        self.small,self.large = [], []

    def addNum(self, num: int) -> None:
        """
        Add a integer number from the data stream to the data structure.
        """
        if self.large and num > self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)


        if len(self.small) > len(self.large) + 1:
            val=  heapq.heappop(self.large)
            heapq.heappush(self.small,-val)
        
        if len(self.large) > len(self.small) + 1:

            val = -heapq.heappop(self.small)
            heapq.heappush(self.large,val)

    def findMedian(self) -> float:
        """
        Return the median of all elements so far.
        """
        if len(self.small) > len(self.large):
                return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0

# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    # The fixture will attempt to construct a working Solution for each test.
    # Tests assume Solution has working __init__, addNum and findMedian methods.
    try:
        return Solution()
    except NotImplementedError:
        # If Solution is not implemented yet, return a placeholder that raises on use
        class Placeholder:
            def __init__(self):
                raise NotImplementedError("Solution not implemented")
        return Placeholder()

def test_median_simple_sequence():
    s = Solution()
    s.addNum(1)
    assert s.findMedian() == 1.0
    s.addNum(2)
    assert s.findMedian() == 1.5
    s.addNum(3)
    assert s.findMedian() == 2.0

def test_median_with_duplicates_and_negatives():
    s = Solution()
    for x in [5, 15, 1, 3]:
        s.addNum(x)
    # Numbers are [5,15,1,3] -> sorted [1,3,5,15], median = (3+5)/2 = 4.0
    assert s.findMedian() == 4.0

    s.addNum(3)
    # Now [1,3,3,5,15] -> median = 3
    assert s.findMedian() == 3.0

    s.addNum(-2)
    # Now [-2,1,3,3,5,15] -> median = (3+3)/2 = 3.0
    assert s.findMedian() == 3.0

def test_median_large_stream():
    s = Solution()
    vals = list(range(1, 101))  # 1..100
    for v in vals:
        s.addNum(v)
    # median of 1..100 is (50 + 51)/2 = 50.5
    assert s.findMedian() == 50.5

def test_median_single_element_and_repeated():
    s = Solution()
    s.addNum(42)
    assert s.findMedian() == 42.0
    s.addNum(42)
    assert s.findMedian() == 42.0
    s.addNum(42)
    assert s.findMedian() == 42.0

def test_median_type_error_and_invalid_usage():
    s = Solution()
    with pytest.raises(TypeError):
        s.addNum(None)  # invalid type
    # If no numbers added, behavior is unspecified; we accept either an Exception or a float result.
    try:
        _ = s.findMedian()
        assert isinstance(_, float)
    except Exception:
        assert True

