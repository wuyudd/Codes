# 200. Number of Islands
    # Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
    #   An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    #   You may assume all four edges of the grid are all surrounded by water.

# My solution: DFS and update the visited position


class Solution(object):
    def num_of_islands(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, m, n, i, j)
        return res

    def dfs(self, grid, m, n, x, y):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0': # ending condition
            return
        grid[x][y] = '0'
        self.dfs(grid, m, n, x-1, y)
        self.dfs(grid, m, n, x+1, y)
        self.dfs(grid, m, n, x, y-1)
        self.dfs(grid, m, n, x, y+1)


s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(s.num_of_islands(grid))