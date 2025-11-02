import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Helper to build a binary tree from level-order list representation."""
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
    """Run the first example manually."""
    root = build_tree([1, 2, 3])
    print("Example 1:")
    print("Input: root = [1,2,3]")
    print("Expected Output: 25")
    sol = Solution()
    try:
        result = sol.sumNumbers(root)
        print("Result:", result)
    except NotImplementedError:
        print("sumNumbers() is not yet implemented.")


@pytest.fixture(params=[
    ([1, 2, 3], 25),
    ([4, 9, 0, 5, 1], 1026)
])
def tree_and_expected(request):
    tree_vals, expected = request.param
    root = build_tree(tree_vals)
    return root, expected


def test_sum_numbers(tree_and_expected):
    root, expected = tree_and_expected
    sol = Solution()
    sol.sumNumbers(root)


class Solution:
    def sumNumbers(self, root):
        """Return the total sum of all root-to-leaf numbers."""
        
        def dfs(cur,num):
            if not cur:
                return 0

            num = num*10 + cur.val
            if not cur.left and not cur.right:
                return num
            return dfs(cur.left,num) + dfs(cur.right,num)


        return dfs(root,0)
    



if __name__ == "__main__":
    main()

