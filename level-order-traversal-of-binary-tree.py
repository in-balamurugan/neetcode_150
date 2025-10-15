# test_level_order_traversal.py
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
        ([1,2,3,4,5,6,7], [[1],[2,3],[4,5,6,7]]),  # Example 1
        ([], []),                                                  # Empty tree
        ([1], [[1]]),                                              # Single node
    ],
)
def test_level_order(inp, expected):
    root = list_to_tree(inp)
    sol = Solution()
    assert sol.levelOrder(root) == expected

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        q=deque()
        q.append(root)

        while q:
            qLen=len(q)

            level=[]

            for _ in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        return res



                



        
