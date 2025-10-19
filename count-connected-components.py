import pytest

# main function to "run" the first example (prints the example and expected output)
# Placed before the Solution class as requested.
def main():
    n = 3
    edges = [[0, 1], [0, 2]]
    print("Example 1 Input:", f"n={n}", f"edges={edges}")
    # We print the expected output for the example (do not call Solution since it's intentionally unimplemented)
    print("Output:", 1)

# Call main at module import as requested.
main()


# -------- PyTest tests --------
# Single fixture with params containing the provided (input, expected) pairs.
@pytest.fixture(params=[
    ({'n': 3, 'edges': [[0, 1], [0, 2]]}, 1),
    ({'n': 6, 'edges': [[0, 1], [1, 2], [2, 3], [4, 5]]}, 2),
])
def example_cases(request):
    """Fixture yielding (input_dict, expected) pairs."""
    return request.param


def test_count_components(example_cases):
    (input_dict, expected) = example_cases
    n = input_dict['n']
    edges = input_dict['edges']

    sol = Solution()
    assert sol.countComponents(n, edges) == expected


# -------- Solution placeholder (must be at the bottom) --------
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        """Return the number of connected components in an undirected graph.
        This method is intentionally unimplemented for the exercise.
        """
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res
