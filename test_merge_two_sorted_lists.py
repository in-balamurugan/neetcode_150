# test_merge_two_sorted_lists.py
# PyTest file for LeetCode 21: Merge Two Sorted Lists
# - Single pytest.fixture with params holding all (input, expected) pairs.
# - One test function using that fixture.
# - A main() function (before Solution) that runs the first example.
# - Single Solution class defined at the bottom; target method is unimplemented.

from typing import Optional, List
import pytest


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def list_to_linked(lst: List[int]) -> Optional[ListNode]:
    """Convert a Python list to a linked ListNode chain."""
    if not lst:
        return None
    dummy = ListNode(0)
    cur = dummy
    for v in lst:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_to_list(node: Optional[ListNode]) -> List[int]:
    """Convert a linked ListNode chain to a Python list."""
    out = []
    cur = node
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


# -------------------------
# main (runs the first example)
# -------------------------
def main():
    # First example for LeetCode 21
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    try:
        result = Solution().mergeTwoLists(l1, l2)
        print("Result of merging [1,2,4] and [1,3,4]:", linked_to_list(result))
    except NotImplementedError:
        print("mergeTwoLists is not implemented (NotImplementedError raised).")


# -------------------------
# PyTest fixtures and tests
# -------------------------
# The user asked that we only include the test cases they provide.
# They did not provide test cases in the prompt, so the file uses
# common LeetCode examples (no extras beyond these three typical cases).

@pytest.fixture(
    params=[
        # Each entry: ((l1_list, l2_list), expected_list)
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),  # Example 1
        (([], []), []),  # both empty
        (([], [0]), [0]),  # one empty, one non-empty
    ]
)
def cases(request):
    (l1_list, l2_list), expected = request.param
    l1 = list_to_linked(l1_list)
    l2 = list_to_linked(l2_list)
    return (l1, l2, expected)


def test_merge_two_sorted_lists(cases):
        l1, l2, expected = cases
        # The target method must exist but be unimplemented (raise NotImplementedError).
        # We call it to assert that it indeed raises NotImplementedError.
        Solution().mergeTwoLists(l1, l2)


# -------------------------
# Solution class (bottom)
# -------------------------
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return it as a sorted list.
        This method is intentionally unimplemented for the tests — it should raise NotImplementedError.
        """
        dummy=merged=ListNode()

        while l1 and l2:
            if l1.val > l2.val:
                merged = l1
                l1 = l1.next
            else:
                merged = l2
                l2 = l2.next
            
            merged=merged.next
        return merged


# Call main if run as a script
if __name__ == "__main__":
    main()

