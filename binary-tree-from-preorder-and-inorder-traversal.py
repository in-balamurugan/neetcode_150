# test_build_tree.py
import pytest
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val, self.left, self.right = val, left, right

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to level-order list representation for testing."""
    if not root:
        return []
    from collections import deque
    q, out = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # Trim trailing None values
    while out and out[-1] is None:
        out.pop()
    return out

@pytest.mark.parametrize(
    "preorder, inorder, expected",
    [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),  # Example 1
        ([-1], [-1], [-1]),                                                    # Single node
    ],
)
def test_build_tree(preorder, inorder, expected):
    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    assert tree_to_list(root) == expected

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Build binary tree from preorder and inorder traversal.
        """
        # put inorder hash
        indices = {val: idx for idx,val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(l,r):

            if l>r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid= indices[root_val]
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)

            return root
        return dfs(0, len(inorder)-1)


