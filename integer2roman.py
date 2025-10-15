import pytest
from typing import Tuple


@pytest.fixture(params=[
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
])
def cases(request) -> Tuple[int, str]:
    return request.param


def test_int_to_roman(cases):
    num, expected = cases
    assert Solution().intToRoman(num) == expected


def main():
    example = 3
    print(f"Running example: num = {example}")
    try:
        result = Solution().intToRoman(example)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.intToRoman is not implemented yet.")


class Solution:
    def intToRoman(self, num: int) -> str:
        """Convert an integer to a Roman numeral. Not implemented."""
        
        symList = [
            ["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
            ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
            ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
            ["M", 1000]
        ]

        res =""

        for sym,val in reversed(symList):
            count = num // val
            if count:
                res += count*sym
                num = num % val
        return res

if __name__ == "__main__":
    main()

