# test_is_balanced.py
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
    Build a binary tree from a level-order list where None represents a missing node.
    Example: [1,2,3,None,4] -> root=1, left=2, right=3, and 2.right=4
    """
    if not level_order:
        return None

    iter_vals = iter(level_order)
    root_val = next(iter_vals)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    queue: deque[TreeNode] = deque([root])

    # Process pairs of children for each parent in FIFO order
    for val_left, val_right in zip(iter_vals, iter_vals):
        parent = queue.popleft()

        if val_left is not None:
            parent.left = TreeNode(val_left)
            queue.append(parent.left)

        if val_right is not None:
            parent.right = TreeNode(val_right)
            queue.append(parent.right)

    # If there's one leftover value (odd length), attach it as a left child of next parent
    try:
        last_left = next(iter_vals)
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
        (([3, 9, 20, None, None, 15, 7],), True),
        # Example 2
        (([1, 2, 2, 3, 3, None, None, 4, 4],), False),
        # Example 3
        (([],), True),
    ]
)
def case(request) -> Tuple[Tuple[List[Optional[int]]], bool]:
    """
    Each param is ((level_order_list,), expected_bool)
    """
    return request.param


def test_is_balanced(case):
    (level_order,), expected = case
    root = build_tree(level_order)
    sol = Solution()
    result = sol.isBalanced(root)
    assert result == expected


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if a binary tree is height-balanced.
        (Unimplemented — raise NotImplementedError as requested.)
        """
        
        def dfs(root):
            if not root:
                return [True,0]

            left=dfs(root.left)
            right=dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1])  <= 1

            return [balanced,1+max(left[1],right[1])]

        return dfs(root)[0]

# ------------------------------------------------------------------
# Simple manual test runner for the first case
# ------------------------------------------------------------------
def main():
    level_order = [3, 9, 20, None, None, 15, 7]
    expected = True
    root = build_tree(level_order)
    sol = Solution()

    try:
        result = sol.isBalanced(root)
    except NotImplementedError:
        print("❌ isBalanced is not implemented yet.")
        return

    print(f"Input tree (level order): {level_order}")
    print(f"Expected: {expected}")
    print(f"Result:   {result}")
    print("✅ Test passed!" if result == expected else "❌ Test failed.")


if __name__ == "__main__":
    main()

