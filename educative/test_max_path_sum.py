import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Build a binary tree from a level-order list representation where None
    indicates missing nodes.
    Example: [1, 2, 3, None, 4] builds:
         1
        / \
       2   3
        \
         4
    """
    if not values:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def main():
    """Run the first example manually and print the result."""
    root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    targetSum = 8
    print("Example 1:")
    print("Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8")
    print("Expected Output: 3")
    sol = Solution()
    try:
        result = sol.pathSum(root, targetSum)
        print("Result:", result)
    except NotImplementedError:
        print("pathSum() is not yet implemented.")


@pytest.fixture(params=[
    # (tree values, targetSum, expected)
    ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
    ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3)
])
def tree_and_target(request):
    vals, target, expected = request.param
    root = build_tree(vals)
    return root, target, expected


def test_path_sum_not_implemented(tree_and_target):
    """
    The Solution.pathSum method is intentionally unimplemented for this scaffold
    and should raise NotImplementedError when called. This test uses the
    examples provided in the prompt.
    """
    root, target, expected = tree_and_target
    sol = Solution()
    sol.pathSum(root, target)


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """
        Return the number of downward paths where the sum of node values equals
        targetSum. This method is intentionally left unimplemented for the test
        scaffold and should raise NotImplementedError.
        """
        
        def dfs(node,path_sums):
            if not node:
                return 0

            path_sums = [node.val + s for s in path_sums] + [node.val]
            count = path_sums.count(targetSum)
    
            count += dfs(node.left, path_sums) + dfs(node.right, path_sums)

            return count


        return dfs(root,[])

if __name__ == "__main__":
    main()

