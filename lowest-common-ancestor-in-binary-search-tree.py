# test_lowest_common_ancestor_bst.py
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
    "inp, p_val, q_val, expected",
    [
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6),  # Example 1
        ([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2),  # Example 2
    ],
)
def test_lowest_common_ancestor(inp, p_val, q_val, expected):
    root = list_to_tree(inp)

    # locate nodes by value
    def find_node(node, val):
        if not node:
            return None
        if node.val == val:
            return node
        return find_node(node.left, val) or find_node(node.right, val)

    p, q = find_node(root, p_val), find_node(root, q_val)

    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p, q)
    assert ans.val == expected


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q: return None
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root

