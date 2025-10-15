# test_serialize_deserialize.py
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

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """Converts a binary tree to level-order list representation."""
    if not root:
        return []
    q, out = deque([root]), []
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    # Trim trailing None values
    while out and out[-1] is None:
        out.pop()
    return out

@pytest.mark.parametrize(
    "inp",
    [
        [1, 2, 3, None, None, 4, 5],   # Example 1
        [],                            # Empty tree
        [1],                           # Single node
    ],
)
def test_serialize_deserialize(inp):
    root = list_to_tree(inp)
    codec = Codec()
    data = codec.serialize(root)
    new_root = codec.deserialize(data)
    assert tree_to_list(new_root) == inp

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        TODO: implement

        """
        res= []

        def dfs(node):
            if not node:
                res.append("N")
                return
        
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)


        
        dfs(root)

        return ",".join(res)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        TODO: implement
        """
        vals = data.split(",")
        self.i=0
            
        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None

            print(vals,self.i)            
            node = TreeNode(int(vals[self.i]))
            self.i +=1
            node.left= dfs()
            node.right= dfs()
            return node

        return dfs()

