# test_good_nodes.py
from collections import deque
from typing import Optional, List, Tuple
import pytest

# Helper TreeNode definition and builder
class TreeNode:
    def __init__(self, val: int=0, left: 'TreeNode'=None, right: 'TreeNode'=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level_list: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from level-order list where None represents missing nodes."""
    if not level_list:
        return None
    it = iter(level_list)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    while q:
        node = q.popleft()
        try:
            left_val = next(it)
        except StopIteration:
            break
        if left_val is not None:
            node.left = TreeNode(left_val)
            q.append(node.left)
        try:
            right_val = next(it)
        except StopIteration:
            break
        if right_val is not None:
            node.right = TreeNode(right_val)
            q.append(node.right)
    return root

# main to test the first example (placed above Solution as requested)
def main():
# First example: root = [2,1,1,3,null,1,5], expected output 3

    example = [2, 1, 1, 3, None, 1, 5]
    root_example = build_tree(example)
    print("Running main test for first example (will raise NotImplementedError since method is unimplemented):")
    print(Solution().goodNodes(root_example))  # this will raise NotImplementedError

# PyTest fixture with params containing only the provided (input, expected) pairs
@pytest.fixture(params=[
    # Example 1
    ([2, 1, 1, 3, None, 1, 5], 3),
    # Example 2
    ([1, 2, -1, 3, 4], 4),
])
def cases(request) -> Tuple[List[Optional[int]], int]:
    return request.param

# Single test function that uses the fixture
def test_good_nodes(cases):
    level_list, expected = cases
    root = build_tree(level_list)
    result = Solution().goodNodes(root)
    assert result == expected

# Single Solution class at the bottom with the target method unimplemented
class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """
        Count "good" nodes in binary tree.
        A node x is good if in the path from root to x there is no node with value greater than x.val.
        """
        def dfs(node,maxVal):
            print(node,maxVal)
            if not node:
                return 0

            res = 1 if node.val>= maxVal else 0
            maxVal = max(maxVal,node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return  dfs(root,root.val)

if __name__ == '__main__':
    main()
