#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

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
    "root_list, sub_list, expected",
    [
        # Example 1
        ([3, 4, 5, 1, 2], [4, 1, 2], True),
        # Example 2
        ([3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False),
    ],
)
def test_is_subtree(root_list, sub_list, expected):
    root = list_to_tree(root_list)
    subRoot = list_to_tree(sub_list)
    sol = Solution()  
    assert sol.isSubtree(root, subRoot) == expected


class Solution:
    def isSubtree(self,root,subRoot):
        
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return  (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSameTree(self,root,subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (self.isSameTree(root.left, subRoot.left) and
                   self.isSameTree(root.right, subRoot.right))

        return False














