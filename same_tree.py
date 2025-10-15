# test_same_tree.py
import pytest
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode|None" = None, right: "TreeNode|None" = None):
        self.val, self.left, self.right = val, left, right

def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data: 
        return None
    root = TreeNode(data[0])
    q, i = deque([root]), 1
    while q and i < len(data):
        node = q.popleft()
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i]); q.append(node.left)
        i += 1
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i]); q.append(node.right)
        i += 1
    return root

@pytest.mark.parametrize(
    "p_list, q_list, expected",
    [
        ([1, 2, 3], [1, 2, 3], True),          # Example 1
        ([1, 2], [1, None, 2], False),         # Example 2
        ([1, 2, 1], [1, 1, 2], False),         # Example 3
    ],
)
def test_same_tree(p_list, q_list, expected):
    p = list_to_tree(p_list)
    q = list_to_tree(q_list)
    sol = Solution()   
    assert sol.isSameTree(p, q) == expected

class Solution:
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not(p and q and p.val == q.val):
            return False

        if self.isSameTree(p.left,q.left) == False:
            return False
        if self.isSameTree(p.right,q.right) == False:
            return False
        return True



