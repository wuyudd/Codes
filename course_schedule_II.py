# lc 210. Course Schedule II
    # Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

# My solution: topological sorting

import collections


class Solution:
    def findOrder(self, numCourses, prerequisites):
        indegree = {}
        connected = {}
        res = []
        for i in range(numCourses):
            indegree[i] = indegree.get(i, 0)
            connected[i] = set()
        for ele in prerequisites:
            indegree[ele[0]] += 1
            connected[ele[1]].add(ele[0])

        queue = collections.deque()

        for key, val in indegree.items():
            if val == 0:
                queue.appendleft(key)

        while queue:
            curr = queue.pop()
            res.append(curr)
            for ele in connected[curr]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    queue.appendleft(ele)
        if len(res) != numCourses:
            return []
        return res

