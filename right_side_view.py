import pytest
from typing import List, Optional, Tuple
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list where None represents a missing node."""
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


@pytest.fixture(params=[
    # Example 1
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
    # Example 2
    ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
    # Example 3
    ([1, None, 3], [1, 3]),
    # Example 4
    ([], []),
])
def case(request) -> Tuple[Optional[TreeNode], List[int]]:
    vals, expected = request.param
    root = build_tree(list(vals))
    return root, expected


def test_right_side_view(case: Tuple[Optional[TreeNode], List[int]]):
    root, expected = case
    sol = Solution()
    assert sol.rightSideView(root) == expected


# The Solution class must be defined at the bottom of the file.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q=deque()
        res=[]

        if root is None:
            return []
        q.append(root)

        while q:
            level_size = len(q)
            for i in range(len(q)):
                print(i)
                node = q.popleft()
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None

                if i == level_size-1:
                    res.append(node.val)
        return res

if __name__ == "__main__":
    # Manually test the first case
    values = [1, 2, 3, None, 5, None, 4]
    expected = [1, 3, 4]
    root = build_tree(values)
    sol = Solution()
    try:
        output = sol.rightSideView(root)
    except NotImplementedError:
        output = "Method not implemented"
    print(f"Input: {values}\nExpected: {expected}\nOutput: {output}")
