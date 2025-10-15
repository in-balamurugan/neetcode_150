# test_max_path_sum.py
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
        ([-10, 9, 20, None, None, 15, 7], 42),  # Example 1
        ([1, 2, 3], 6),                        # Example 2
        ([1, -2, -3], 1),                      # Max path is just [1]
    ],
)
def test_max_path_sum(inp, expected):
    root = list_to_tree(inp)
    sol = Solution()
    assert sol.maxPathSum(root) == expected

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Return maximum path sum in the binary tree.
        TODO: implement
        """
        raise NotImplementedError

