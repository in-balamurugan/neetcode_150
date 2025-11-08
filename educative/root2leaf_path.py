import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_example_tree():
    """
    Build a tree that contains the path 5 -> 2 -> 4 -> 8 (root-to-leaf)
    but does NOT contain the path 5 -> 3 -> 4 -> 9.

    Structure (visual):
            5
           / \
          2   3
           \   \
            4   4
             \
              8

    This matches the examples in the prompt.
    """
    n8 = TreeNode(8)
    n4_right = TreeNode(4, None, n8)   # 4 -> right -> 8
    n2 = TreeNode(2, None, n4_right)  # 2 -> right -> 4
    n4_left_of_3 = TreeNode(4)        # 4 (no child 9)
    n3 = TreeNode(3, None, n4_left_of_3)
    root = TreeNode(5, n2, n3)
    return root


def main():
    """Run the first example manually and print the result."""
    root = build_example_tree()
    arr = [5, 2, 4, 8]
    print("Example 1:")
    print("Input: arr =", arr)
    print("Expected Output: True")
    sol = Solution()
    try:
        result = sol.is_valid_sequence(root, arr)
        print("Result:", result)
    except NotImplementedError:
        print("is_valid_sequence() is not yet implemented.")


@pytest.fixture(params=[
    # (root-builder function, input sequence array, expected boolean)
    (build_example_tree, [5, 2, 4, 8], True),
    (build_example_tree, [5, 3, 4, 9], False)
])
def tree_and_sequence(request):
    builder, seq, expected = request.param
    root = builder()
    return root, seq, expected


def test_is_valid_sequence_raises_not_implemented(tree_and_sequence):
    """
    The Solution.is_valid_sequence method is intentionally unimplemented
    (should raise NotImplementedError). This test uses the provided examples.
    """
    root, seq, expected = tree_and_sequence
    sol = Solution()
    sol.is_valid_sequence(root, seq)


class Solution:
    def is_valid_sequence(self, root: TreeNode, arr: list) -> bool:
        """
        Return True if the given array 'arr' is present as a root-to-leaf
        path in the binary tree with given root.

        NOTE: This method is intentionally left unimplemented for the test
        scaffold and should raise NotImplementedError.
        """
        def dfs(cur, path):
            if not cur:
                return False

            path.append(cur.val)
            if path == arr:
                return True
            return dfs(cur.left, path) or dfs(cur.right, path)

        return dfs(root, [])


if __name__ == "__main__":
    main()

