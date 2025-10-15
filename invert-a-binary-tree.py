# test_invert_tree.py
import pytest
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

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

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left); q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out



@pytest.mark.parametrize(
    "inp, expected",
    [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),  # Example 1
        ([2, 1, 3], [2, 3, 1]),                          # Example 2
        ([], []),                                        # Example 3
    ],
)
def test_invert_examples(inp, expected):
    root = list_to_tree(inp)
    s=Solution()
    inverted = s.invert_binary_tree(root)
    assert tree_to_list(inverted) == expected

class Solution:
    def invert_binary_tree(self,root):

        if not root: return None

        root.left,root.right = root.right,root.left
        self.invert_binary_tree(root.left)
        self.invert_binary_tree(root.right)
        
        return root
        

