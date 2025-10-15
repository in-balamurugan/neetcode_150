import pytest
from typing import List, Optional


# Definition for singly-linked list node used in tests.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next


def build_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def lists_equal(l: Optional[ListNode], vals: List[int]) -> bool:
    cur = l
    i = 0
    while cur and i < len(vals):
        if cur.val != vals[i]:
            return False
        cur = cur.next
        i += 1
    return cur is None and i == len(vals)


@pytest.fixture(params=[
    # Example 1
    ([[1,4,5], [1,3,4], [2,6]], [1,1,2,3,4,4,5,6]),
    # Example 2: empty input -> empty output
    ([], []),
    # Example 3: list containing one empty list -> empty output
    ([[]], []),
])
def cases(request):
    return request.param


def test_merge_k_sorted_lists(cases):
    lists, expected = cases
    input_lists = [build_list(lst) for lst in lists]
    result = Solution().mergeKLists(input_lists)
    assert lists_equal(result, expected)


def main():
    example = [[1,4,5], [1,3,4], [2,6]]
    print(f"Running example: lists = {example}")
    try:
        input_lists = [build_list(lst) for lst in example]
        result = Solution().mergeKLists(input_lists)
        # Convert result to Python list for printing
        out = []
        cur = result
        while cur:
            out.append(cur.val)
            cur = cur.next
        print(f"Result: {out}")
    except NotImplementedError:
        print("Solution.mergeKLists is not implemented yet.")


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        def mergeList(list1,list2):
            temp=ListNode()
            dummy=temp

            while list1 and list2:
                if list1.val < list2.val:
                    temp.next=list1
                    list1  = list1.next
                else:
                    temp.next=list2
                    list2 = list2.next

                temp=temp.next

            if list1:
                temp.next = list1

            if list2:
                temp.next = list2
            

            return dummy.next


        while len(lists)>1:

            
            merged_list=[]
            for i in range(0,len(lists),2):
                
                print(len(lists))
                l1=lists[i]
                l2=lists[i+1] if i+1 < len(lists) else None
                merged_list.append(mergeList(l1,l2))
            lists=merged_list


        return lists[0] if lists else None
        









if __name__ == "__main__":
    main()

