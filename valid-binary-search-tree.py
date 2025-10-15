# test_validate_bst.py
import pytest
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val, self.left, self.right = val, left, right

def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from level-order list representation."""
    if not data:
        return None
    root = TreeNode(data[0])
    q, i = deque([root]), 1
    while q and i < len(data):
        node = q.popleft()
        if i < len(data) and data[i] is not None:
            node.left = TreeNode(data[i])
            q.append(node.left)
        i += 1
        if i < len(data) and data[i] is not None:
            node.right = TreeNode(data[i])
            q.append(node.right)
        i += 1
    return root

@pytest.mark.parametrize(
    "inp, expected",
    [
        ([2, 1, 3], True),            # Valid BST
        ([5, 1, 4, None, None, 3, 6], False),  # Invalid BST
        ([], True),                   # Empty tree is valid
        ([1], True),                  # Single node
    ],
)
def test_is_valid_bst(inp, expected):
    root = list_to_tree(inp)
    sol = Solution()
    assert sol.isValidBST(root) == expected

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(left,node,right):
            if not node:
                return True

            if not(left < node.val < right):
                return False
            
            return valid(left, node.left,node.val) and valid(node.val,node.right,right)

        return valid(float("-inf"),root,float("inf"))

