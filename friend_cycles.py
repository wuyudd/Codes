# LC 547. Friend Circles

# also pay attention to subarray problems:
#   825. Friends Of Appropriate Ages

#####################################################################################
# my solution:
# idea: dfs, save visited rows to visited list

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        counter = 0
        visited = [0 for i in range(len(M))]
        for i in range(len(M)):
            if visited[i] == 0:
                self.dfs(M, i, visited)
                counter += 1
        return counter

    def dfs(self, M, i, visited):
        for j in range(len(M[i])):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, j, visited)

#####################################################################################