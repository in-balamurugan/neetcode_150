# reverse_linked_list_test.py
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
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverse a singly linked list.

        Example:
        Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
        Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
        """
        curr,prev = head,None

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
            



# ---------- Helper functions ----------
def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "values, expected",
    [
        ([1,2,3,4,5], [5,4,3,2,1]),   # typical case
        ([], []),                     # empty list
        ([1], [1]),                   # single element
        ([1,2], [2,1]),               # two elements
    ],
)
def test_reverse_linked_list(solver, values, expected):
    head = build_linked_list(values)
    reversed_head = solver.reverseList(head)
    assert linked_list_to_list(reversed_head) == expected

