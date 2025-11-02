import pytest
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a list using level-order insertion where None indicates missing nodes.
    Example: [1,2,3,None,4]"""
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


@pytest.fixture(params=[
    # Example 1
    ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True),
    # Example 2
    ([1,2,3], 5, False),
    # Example 3
    ([], 0, False),
])
def case(request):
    vals, target, expected = request.param
    root = build_tree(vals)
    return root, target, expected


def test_has_path_sum(case):
    root, target, expected = case
    sol = Solution()
    assert sol.hasPathSum(root, target) == expected


def main():
    # Run the first example and print the result (for manual execution)
    vals = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    target = 22
    root = build_tree(vals)
    sol = Solution()
    try:
        result = sol.hasPathSum(root, target)
    except NotImplementedError:
        print("Solution.hasPathSum is not implemented yet.")
        return
    print(f"Result for example 1: {result}")


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Target method - intentionally unimplemented for the test scaffold."""
        
        if not root:
            return False

        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0

        return self.hasPathSum(root.left,targetSum)  or self.hasPathSum(root.right,targetSum)


if __name__ == "__main__":
    main()

