# merge_k_sorted_lists_test.py
import pytest
import heapq

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
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        Merge k sorted linked lists and return it as one sorted list.

        Example:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        """
        #divide and conquer the list
        if not lists or len(lists) == 0:
            return None 

        while len(lists)>1:
            merged_list=[]
            for i in range(0, len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1<len(lists) else None
                merged_list.append(self.merge_list(l1,l2))
            lists=merged_list
        
        return lists[0]

    def merge_list(self,l1,l2):

        tail=ListNode()
        dummy=tail

        while l1 and l2:
            if l1.val<l2.val:
                tail.next=l1
                l1=l1.next

            else:
                tail.next = l2
                l2 = l2.next

            tail=tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

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
    "list_values, expected",
    [
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),  # typical case
        ([], []),                                      # no lists
        ([[]], []),                                    # list with one empty list
        ([[1]], [1]),                                  # single element
        ([[1,2,3],[4,5,6]], [1,2,3,4,5,6]),            # two already sorted lists
        ([[2,2,2],[2,2]], [2,2,2,2,2]),                # duplicates
    ],
)
def test_merge_k_sorted_lists(solver, list_values, expected):
    lists = [build_linked_list(vals) for vals in list_values]
    merged = solver.mergeKLists(lists)
    assert linked_list_to_list(merged) == expected

def test_merge_k_sorted_lists_invalid_type(solver):
    with pytest.raises(TypeError):
        solver.mergeKLists(None)  # invalid input type

