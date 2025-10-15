# test_diameter_of_binary_tree.py
from collections import deque
from typing import Optional, List, Tuple
import pytest


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list representation where None represents a missing node.
    Example: [1, 2, 3, None, 4] -> tree with root=1, left=2, right=3, and 2.right=4
    """
    if not level_order:
        return None

    iter_vals = iter(level_order)
    root_val = next(iter_vals)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue: deque[TreeNode] = deque([root])

    for val_left, val_right in zip(iter_vals, iter_vals):
        parent = queue.popleft()

        if val_left is not None:
            parent.left = TreeNode(val_left)
            queue.append(parent.left)

        if val_right is not None:
            parent.right = TreeNode(val_right)
            queue.append(parent.right)

    # If the list has an odd length, there could be one last left child
    # (pytest cases here don't need it, but this keeps builder robust)
    try:
        last_left = next(iter_vals)  # type: ignore[misc]
        parent = queue.popleft()
        if last_left is not None:
            parent.left = TreeNode(last_left)
            queue.append(parent.left)
    except StopIteration:
        pass

    return root


@pytest.fixture(
    params=[
        # Example 1
        (([1, 2, 3, 4, 5],), 3),
        # Example 2
        (([1, 2],), 1),
    ]
)
def case(request) -> Tuple[Tuple[List[Optional[int]]], int]:
    """
    Each param is a tuple: ((level_order_list,), expected_output)
    The extra tuple layer around the list allows easy extension if the target
    method later took more arguments; tests remain unchanged.
    """
    return request.param


def test_diameter_of_binary_tree(case):
    (level_order,), expected = case
    root = build_tree(level_order)
    sol = Solution()
    result = sol.diameterOfBinaryTree(root)
    assert result == expected


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.
        """
        
        res =0
        
        def dfs(root):

            non local res
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)
            
            return 1 + max(left,right)

        dfs(root)
        return res




