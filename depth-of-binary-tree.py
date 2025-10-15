# test_max_depth.py
import pytest
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val, self.left, self.right = val, left, right

def list_to_tree(data: List[Optional[int]]) -> Optional[TreeNode]:
    if not data: return None
    root = TreeNode(data[0]); q, i = deque([root]), 1
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
    "inp, expected",
    [
        ([1, 2, 3, None, None, 4], 3),  # Example 1
        ([], 0),                        # Example 2
    ],
)
def test_max_depth(inp, expected):
    root = list_to_tree(inp)
    sol = Solution()
    assert sol.maxDepth(root) == expected


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
