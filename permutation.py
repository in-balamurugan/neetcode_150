import pytest

@pytest.fixture(params=[
    # (input_tuple, expected)
    (("abc", "lecabee"), True),   # Example 1
    (("abc", "lecaabee"), False)  # Example 2
])
def case(request):
    (s1, s2), expected = request.param
    return s1, s2, expected

def test_check_inclusion(case):
    s1, s2, expected = case
    sol = Solution()
    assert sol.checkInclusion(s1, s2) == expected

# Single Solution class must be defined at the bottom of the file
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Return True if s2 contains a permutation of s1, otherwise False.

        NOTE: This method is intentionally left unimplemented for the test scaffold.
        """
        if len(s1) > len(s2):
            return False

        s1Count,s2Count = [0]*26, [0]*26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord['a']) += 1
            s2Count[ord[s2[i]) - ord['a']) += 1

            matches = 0

            for i in range(26):
                matches += (1 if s1Count[i] == s2Count[i] else 0)

            l = 0

            for r in range(len(s1), len(s2))
                
                if matches == 26:
                    return True

                index = 
