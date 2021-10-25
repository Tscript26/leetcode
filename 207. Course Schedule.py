"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""
from src import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        不能成环
        :param numCourses:
        :param prerequisites:
        :return:
        """
        if len(prerequisites) > numCourses * (numCourses - 1) // 2:
            return False
        edges = defaultdict(list)
        for p in prerequisites:
            edges[p[1]].append(p[0])
        visited = [0] * numCourses
        valid = True
        results = []
        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            results.append(u)
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        if not valid:
            return False
        print(results)
        return True


if __name__ == '__main__':
    S= Solution()
    numCourses = 4
    prerequisites = [[1,2],[2,3],[3,1],[0,1]]
    res= S.canFinish(numCourses,prerequisites)
    print(res)
