# Save as clone_graph_test.py
# (If you want pytest auto-discovery, rename the file to start with "test_" when running tests.)

from typing import List, Optional
import pytest

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    """
    Solution container for the Clone Graph problem.

    Implement `cloneGraph(self, node: Optional[Node]) -> Optional[Node]`
    to return a deep copy of the given graph node.
    """
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        

        oldToNew ={}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] =copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy


        return dfs(node) if node else None

# ---- Helper for testing ----
def build_graph(adjList: List[List[int]]) -> Optional[Node]:
    if not adjList:
        return None
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for i, neighbors in enumerate(adjList):
        nodes[i].neighbors = [nodes[j - 1] for j in neighbors]
    return nodes[0]

def graph_to_adjList(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []
    from collections import deque
    visited = {}
    q = deque([node])
    while q:
        cur = q.popleft()
        if cur.val in visited:
            continue
        visited[cur.val] = [n.val for n in cur.neighbors]
        for nei in cur.neighbors:
            if nei.val not in visited:
                q.append(nei)
    return [visited.get(i + 1, []) for i in range(len(visited))]


# ---- Tests (ONLY the examples provided) ----

def test_example_1():
    sol = Solution()
    adjList = [[2], [1, 3], [2]]
    node = build_graph(adjList)
    clone = sol.cloneGraph(node)
    assert graph_to_adjList(clone) == [[2], [1, 3], [2]]

def test_example_2():
    sol = Solution()
    adjList = [[]]
    node = build_graph(adjList)
    clone = sol.cloneGraph(node)
    assert graph_to_adjList(clone) == [[]]

def test_example_3():
    sol = Solution()
    adjList = []
    node = build_graph(adjList)
    clone = sol.cloneGraph(node)
    assert graph_to_adjList(clone) == []

