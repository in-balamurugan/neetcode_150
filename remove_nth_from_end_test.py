# remove_nth_from_end_test.py
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        Remove the n-th node from the end of list and return its head.

        Example:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]
        """
        dummy = ListNode(0,head)
        right=head
        left=head

        while n>0:
            right=right.next
            n -= 1

        while right.next:
            left=left.next
            right=right.next

        
        left.next=left.next.next

        return dummy.next



# ---------- Helper functions ----------
def build_linked_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "values, n, expected",
    [
        ([1,2,3,4,5], 2, [1,2,3,5]),  # remove middle-from-end
        ([1], 1, []),                # single node removed -> empty list
        ([1,2], 1, [1]),             # remove last node
        ([1,2], 2, [2]),             # remove head (n == length)
        ([1,2,3], 3, [2,3]),         # remove head when n equals length
        ([1,2,3,4], 4, [2,3,4]),     # remove head (n==len)
    ],
)
def test_remove_nth_from_end_examples(solver, values, n, expected):
    head = build_linked_list(values)
    new_head = solver.removeNthFromEnd(head, n)
    assert linked_list_to_list(new_head) == expected

def test_remove_nth_from_end_invalid_n(solver):
    head = build_linked_list([1,2,3])
    with pytest.raises(Exception):
        # n is larger than length -> expect an error or defined behavior raising Exception
        solver.removeNthFromEnd(head, 10)

def test_remove_nth_from_end_invalid_types(solver):
    with pytest.raises(TypeError):
        solver.removeNthFromEnd(None, None)  # invalid types for both args

