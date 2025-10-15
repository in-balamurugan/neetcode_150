import pytest
from collections import deque
from typing import Optional


# Definition for a binary tree node used in tests.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list where None indicates missing nodes.
    Example: [3,2,3,None,3,None,1]
    """
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for val in it:
        node = q.popleft()
        # left child
        if val is not None:
            node.left = TreeNode(val)
            q.append(node.left)
        else:
            node.left = None
        # right child (get next value if available)
        try:
            val = next(it)
        except StopIteration:
            break
        if val is not None:
            node.right = TreeNode(val)
            q.append(node.right)
        else:
            node.right = None
    return root


@pytest.fixture(params=[
    # Example 1
    (build_tree([3, 2, 3, None, 3, None, 1]), 7),
    # Example 2
    (build_tree([3, 4, 5, 1, 3, None, 1]), 9),
])
def cases(request):
    return request.param


def test_rob(cases):
    root, expected = cases
    assert Solution().rob(root) == expected


def main():
    example = build_tree([3, 2, 3, None, 3, None, 1])
    print(f"Running example: root = [3,2,3,null,3,null,1]")
    try:
        result = Solution().rob(example)
        print(f"Result: {result}")
    except NotImplementedError:
        print("Solution.rob is not implemented yet.")


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return [0,0]

            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            withRoot = root.val + leftPair[1] + rightPair[1]
            withoutRoot = max(leftPair) + max(rightPair)


            return [withRoot, withoutRoot]

        return max(dfs(root))



        
        


        max(dfs(root))

if __name__ == "__main__":
    main()

