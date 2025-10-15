import pytest

# --- PyTest fixtures and tests ---

@pytest.fixture(params=[
    # (input_edges, expected_output)
    ([[1,2],[1,3],[3,4],[2,4]], [2,4]),
    ([[1,2],[1,3],[1,4],[3,4],[4,5]], [3,4]),
])
def case(request):
    """Fixture yielding (edges, expected) pairs."""
    return request.param

def test_find_redundant_connection(case):
    edges, expected = case
    sol = Solution()
    assert sol.findRedundantConnection(edges) == expected


# --- Main runner for the first example (placed before the Solution class) ---

def main():
    """Run the first example. Since the Solution method is intentionally
    unimplemented (raises NotImplementedError), this will print a friendly
    message if the implementation is missing."""
    example_edges = [[1,2],[1,3],[3,4],[2,4]]
    print("Example 1 input:", example_edges)
    try:
        result = Solution().findRedundantConnection(example_edges)
        print("Output:", result)
    except NotImplementedError:
        print("findRedundantConnection is not implemented yet (NotImplementedError).")



# --- Solution class (must be defined at the bottom of the file) ---

class Solution:
    def findRedundantConnection(self, edges):
        """
        Find an edge that can be removed so that the graph is still a tree.
        This method is intentionally left unimplemented for the purposes of the task.
        """
        n=len((edges)
        
        adj =[[] for _ in range(n+1)]

        def dfs(node,par):
            if visit[node]:
                return True
            
            visit[node] = True
            
            for nei in adj[node]:

                if nei == par:
                    continue
                
                if dfs(nei,node) :
                    return True

            return False


        for u,v in edges:
              adj[u].append(v)
              adj[v].append(u)
              visit = [False ] * (n+1)

              if dfs(u,-1):
                    return [u,v]

              return []










if __name__ == "__main__":
    main()
