# 207. Course Schedule
    # There are a total of n courses you have to take, labeled from 0 to n-1.
    # Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
    # Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# My solution1: topological sorting
# My solution2: DFS

# solution1: topological sorting
import collections


class Solution(object):
    def can_finish(self, pre, num):
        indegree = {}
        connected = {}
        queue = collections.deque()
        cnt = 0

        for i in range(num):
            indegree[i] = 0
            connected[i] = set()

        for ele in pre:
            indegree[ele[0]] += 1
            connected[ele[1]].add(ele[0])

        for key, val in indegree.items():
            if val == 0:
                queue.appendleft(key)
                cnt += 1

        while queue:
            curr = queue.pop()
            for ele in connected[curr]:
                indegree[ele] -= 1
                if indegree[ele] == 0:
                    cnt += 1
                    queue.appendleft(ele)

        return cnt == num

# solution2: DFS
class Solution_2(object):
    def can_finish(self, pre, num):
        visited = set()
        explored = set()
        connected = collections.defaultdict(list)

        for u, v in pre:
            connected[u].append(v)

        def dfs(node):
            if node in visited:
                return True
            visited.add(node)
            for child in connected[node]:
                if child not in explored and dfs(child):
                    return True
            visited.remove(node)
            explored.add(node)
            return False

        for i in range(num):
            if dfs(i):
                return False
            return True