# Save as course_schedule_test.py
# (If you want pytest auto-discovery, rename the file to start with "test_" when running tests.)

from typing import List
import pytest

class Solution:
    """
    Solution container for the Course Schedule problem.

    Implement `canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool`
    to return True if it's possible to finish all courses given the prerequisites,
    otherwise return False.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        preMap = defaultdict(list)

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            visiting=set()
        
        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True
            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

# ---- Tests (ONLY the examples provided) ----

def test_example_1():
    sol = Solution()
    numCourses = 2
    prerequisites = [[0, 1]]
    assert sol.canFinish(numCourses, prerequisites) is True

def test_example_2():
    sol = Solution()
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    assert sol.canFinish(numCourses, prerequisites) is False

