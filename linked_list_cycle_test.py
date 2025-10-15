# linked_list_cycle_test.py
import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        Return True if there is a cycle in the linked list. Otherwise, return False.

        Example:
        Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
        Output: True
        """
        if head is None: return False
        if head is not None and not isinstance(head, ListNode): raise TypeError


        fast,slow = head, head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                return True
        return False


# ---------- Helper functions ----------
def build_linked_list(values, pos=-1):
    """
    Build a linked list from values.
    If pos != -1, create a cycle by connecting the tail to the node at index `pos`.
    """
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


# ---------- Tests (pytest) ----------
@pytest.fixture
def solver():
    return Solution()

@pytest.mark.parametrize(
    "values, pos, expected",
    [
        ([3,2,0,-4], 1, True),   # cycle exists
        ([1,2], 0, True),        # cycle of length 2
        ([1], -1, False),        # single node, no cycle
        ([1], 0, True),          # single node, self cycle
        ([1,2,3,4,5], -1, False) # no cycle
    ],
)
def test_linked_list_cycle(solver, values, pos, expected):
    head = build_linked_list(values, pos)
    assert solver.hasCycle(head) == expected

def test_linked_list_cycle_empty(solver):
    assert solver.hasCycle(None) is False

