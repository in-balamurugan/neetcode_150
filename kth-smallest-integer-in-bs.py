# test_kth_smallest_bst.py
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
    "inp, k, expected",
    [
        ([3, 1, 4, None, 2], 1, 1),  # 1st smallest
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),  # 3rd smallest
    ],
)
def test_kth_smallest(inp, k, expected):
    root = list_to_tree(inp)
    sol = Solution()
    assert sol.kthSmallest(root, k) == expected

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        arr =[]
        def dfs(node):

            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k-1]
