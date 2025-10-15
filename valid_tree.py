import pytest
from typing import List, Tuple

# Main function to demonstrate the first example (prints input and expected output).
def main() -> None:
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    expected = True
    print("Example 1:")
    print(f"n = {n}")
    print(f"edges = {edges}")
    print(f"expected = {expected}")
    try:
        # Attempt to call the solution (will raise NotImplementedError as required).
        result = Solution().validTree(n, edges)
        print(f"result = {result}")
    except NotImplementedError:
        print("Solution.validTree is not implemented.")


# --- PyTest fixtures and tests ---
@pytest.fixture(params=[
    # Provided test cases (input, expected)
    ((5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True),
    ((5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False),
])
def case(request) -> Tuple[Tuple[int, List[List[int]]], bool]:
    """Fixture returning ((n, edges), expected) pairs."""
    return request.param


def test_valid_tree(case):
    (n, edges), expected = case
    sol = Solution()
    assert sol.validTree(n, edges) == expected


# --- Solution class (must be at the bottom) ---
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """Determine if the undirected edges make up a valid tree.

        This method is intentionally unimplemented for the purposes of the
        exercise; it must raise NotImplementedError.
        """
        #3 properties 1. Only n-1 edges can exist 2. no cycle to be verified via dfs 3. no of visits == no of nodes

        if len(edges) >  n-1:
            return False
            
        adj =[[] for _ in range(n)]

        print(n,edges)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print(adj)
        visit =set()
        
        def dfs(node,parent):
            
            if node in visit:
                return False

            visit.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                if not dfs(n,node):
                    return False

            return True
        
        con1  = dfs(0,-1) 
        con2 = len(visit) == n

        return con1 and con2



if __name__ == "__main__":
    main()

