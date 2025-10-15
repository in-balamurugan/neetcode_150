# merge_two_sorted_lists_test.py
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge two sorted linked lists and return it as a sorted list.
        The list should be made by splicing together the nodes of the first two lists.

        Example:
        Input: l1 = 1->2->4, l2 = 1->3->4
        Output: 1->1->2->3->4->4
        """
        dummy = node = ListNode()
        if l1 is not None and not isinstance(l1, ListNode): raise TypeError
        if l2 is not None and not isinstance(l2, ListNode): raise TypeError


        while l1 and l2:
            if l1.val<l2.val:
                node.next = l1
                l1=l1.next
            else:
                node.next =  l2
                l2 = l2.next
            node =node.next

        node.next = l1 or l2

        return dummy.next

                




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
    "a, b, expected",
    [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),  # typical merge
        ([], [], []),                       # both empty
        ([], [0], [0]),                     # one empty, one single element
        ([1,3,5], [2,4,6], [1,2,3,4,5,6]),  # interleaved
        ([1,2,3], [], [1,2,3]),             # other side empty
        ([1], [1], [1,1]),                  # equal single elements
    ],
)
def test_merge_two_sorted_lists(solver, a, b, expected):
    l1 = build_linked_list(a)
    l2 = build_linked_list(b)
    merged = solver.mergeTwoLists(l1, l2)
    assert linked_list_to_list(merged) == expected

def test_merge_two_sorted_lists_type_errors(solver):
    with pytest.raises(TypeError):
        solver.mergeTwoLists(None, None)  # expecting ListNode or empty list built via helper

