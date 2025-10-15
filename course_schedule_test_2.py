import pytest

# --- PyTest fixtures and tests ---

@pytest.fixture(params=[
    # (numCourses, prerequisites, expected_output)
    (3, [[1,0]], [0,1,2]),
    (3, [[0,1],[1,2],[2,0]], []),
])
def case(request):
    return request.param

def test_find_order(case):
    numCourses, prerequisites, expected = case
    sol = Solution()
    assert sol.findOrder(numCourses, prerequisites) == expected


# --- Main runner for the first example (placed before the Solution class) ---

def main():
    """Run the first example manually."""
    numCourses = 3
    prerequisites = [[1,0]]
    print("Example 1 input:", {"numCourses": numCourses, "prerequisites": prerequisites})
    try:
        result = Solution().findOrder(numCourses, prerequisites)
        print("Output:", result)
    except NotImplementedError:
        print("findOrder is not implemented yet (NotImplementedError).")



# --- Solution class (must be defined at the bottom of the file) ---

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        """
        Return a valid ordering of courses or [] if impossible.
        Method intentionally left unimplemented for the task.
        """
        prereq = {c : [] for c in range(numCourses)}
        print(prereq)

        for crs,pre in prerequisites:
            prereq[crs].append(pre)

        print(prereq)

        visit,cycle =set(),set()
        output =[]

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visit.add(crs)
            #print(visit)
            output.append(crs)
            print(output)

            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

if __name__ == "__main__":
    main()
