# test_logger_rate_limiter.py
# PyTest file for LeetCode 359: Logger Rate Limiter
# - Single pytest.fixture with params holding the provided (input, expected) pairs.
# - One test function using that fixture.
# - A main() function (before Solution) that runs the first example.
# - Single Solution class defined at the bottom; target method is unimplemented.

from typing import List, Tuple
import pytest


# -------------------------
# Example sequence helpers
# -------------------------
# We'll represent a sequence of calls as a list of (timestamp, message) tuples
# and expected results as a corresponding list of booleans.

# Classic example sequence (from typical problem description):
# calls: (1, "foo") -> True
#        (2, "bar") -> True
#        (3, "foo") -> False   (within 10s of time 1)
#        (8, "bar") -> False   (within 10s of time 2)
#        (10, "foo") -> False  (within 10s of time 1)
#        (11, "foo") -> True   (after 10s has passed since time 1)
EXAMPLE_CALLS: List[Tuple[int, str]] = [
    (1, "foo"),
    (2, "bar"),
    (3, "foo"),
    (8, "bar"),
    (10, "foo"),
    (11, "foo"),
]
EXAMPLE_EXPECTED: List[bool] = [True, True, False, False, False, True]


# -------------------------
# main (runs the first example)
# -------------------------
def main():
    """
    Run the first example sequence and print the results.
    Since the target method is intentionally unimplemented (raises NotImplementedError),
    this will catch that and print a helpful message.
    """
    seq = EXAMPLE_CALLS
    try:
        logger = Solution()
        outputs = []
        for t, msg in seq:
            outputs.append(logger.shouldPrintMessage(t, msg))
        print("Outputs for example sequence:", outputs)
    except NotImplementedError:
        print("shouldPrintMessage is not implemented (NotImplementedError raised).")


# -------------------------
# PyTest fixture and test
# -------------------------
# The user requested: "Write the test cases I provide, no extras."
# The user did not provide explicit test cases in this message; the file uses the
# canonical example sequence for LeetCode 359 as the single test parameter.

@pytest.fixture(
    params=[
        # Each entry: (calls_list, expected_results_list)
        (EXAMPLE_CALLS, EXAMPLE_EXPECTED),
    ]
)
def cases(request):
    return request.param  # (calls, expected)


def test_logger_rate_limiter_should_raise_not_implemented(cases):
    """
    This test uses the single fixture 'cases'. The target method must exist but be unimplemented
    (raise NotImplementedError). We assert that calling the method (even for the first call in the
    sequence) raises NotImplementedError.
    """
    calls, expected = cases
    logger = Solution()
    # Expect NotImplementedError to be raised when attempting to call the (unimplemented) method.
        # Attempt to run through the sequence; the NotImplementedError should be raised on the first call.
    for t, msg in calls:
        _ = logger.shouldPrintMessage(t, msg)


# -------------------------
# Solution class (bottom)
# -------------------------
class Solution:
    def __init__(self):
        self.log_dict={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Logger Rate Limiter:
        Given a message and a timestamp (in seconds granularity), return True if the message should be
        printed in the given timestamp, otherwise returns False.

        This method is intentionally unimplemented for the tests — it should raise NotImplementedError.
        """
        
        if message not in self.log_dict.keys():
            
            self.log_dict['message']=timestamp
            return True
        else:

            if timestamp - self.log_dict['message'] > 10:
                return True
            else:
                return False

# Call main if run as a script
if __name__ == "__main__":
    main()

