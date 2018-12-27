# lc 694. Number of Distinct Islands
    # An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
    # variant of num_islands

# My solution: record the diff of coordinates from the upper-left element which records the relative positions


class Solution(object):
    def num_distinct_islands(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = set()
        for i in range(m):
            for j in range(n):
                tmp_str = self.dfs(grid, i, j, i, j, m, n, "")
                if tmp_str:
                    res.add(tmp_str)
        return len(res)

    def dfs(self, grid, o_x, o_y, x, y, m, n, tmp_res):
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
            return
        grid[x][y] = 0
        tmp_res += (str(x - o_x) + str(y - o_y))
        self.dfs(grid, o_x, o_y, x-1, y, m, n, tmp_res)
        self.dfs(grid, o_x, o_y, x+1, y, m, n, tmp_res)
        self.dfs(grid, o_x, o_y, x, y-1, m, n, tmp_res)
        self.dfs(grid, o_x, o_y, x, y+1, m, n, tmp_res)
        return tmp_res


s = Solution()
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(s.num_distinct_islands(grid))