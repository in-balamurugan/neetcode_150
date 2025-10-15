# reorder_list_test.py
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Reorder list in-place to follow pattern:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

        Do not return anything; modify the list in-place.

        Example:
        Input: 1->2->3->4
        Output (modified list): 1->4->2->3
        """
        raise NotImplementedError("Implement this method in the Solution class")


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "values, expected",
    [
        ([1,2,3,4], [1,4,2,3]),         # even length
        ([1,2,3,4,5], [1,5,2,4,3]),     # odd length
        ([], []),                       # empty list
        ([1], [1]),                     # single element
        ([1,2], [1,2]),                 # two elements (reordering results same shape)
        ([1,2,3], [1,3,2]),             # small odd
    ],
)
def test_reorder_list_inplace(solver, values, expected):
    head = build_linked_list(values)
    res = solver.reorderList(head)
    # LeetCode's reorderList returns None and modifies in-place.
    # Accept either None return or returning the new head — check mutated list either way.
    if res is None:
        mutated_head = head
    else:
        mutated_head = res
    assert linked_list_to_list(mutated_head) == expected

def test_reorder_list_type_error(solver):
    with pytest.raises(TypeError):
        # invalid type for head should raise
        solver.reorderList(None, "unexpected_arg")  # passing wrong signature on purpose

