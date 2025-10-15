import pytest
from typing import Tuple


@pytest.fixture(params=[
    ("A", 1),
    ("AB", 28),
    ("ZY", 701),
    ("FXSHRXW", 2147483647),
])
def cases(request) -> Tuple[str, int]:
    return request.param


def test_title_to_number(cases):
    column_title, expected = cases
    assert Solution().titleToNumber(column_title) == expected


def main():
    example = "A"
    print(f"Running example: columnTitle = '{example}'")
    try:
        result = Solution().titleToNumber(example)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.titleToNumber is not implemented yet.")


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """Convert Excel column title to corresponding number. Not implemented."""
        
        res=0
        for i,c in enumerate(reversed(columnTitle)):
                res += (i+1)*26 + (ord(c)-64)
        return res

if __name__ == "__main__":
    main()

