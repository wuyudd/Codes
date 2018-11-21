"""
I want to input a matrix size N x N and cut a slice such that each element is
directly below, left-below or right-below the one above it.
And cost is the sum of all elements in the slice.
Eg. matrix is given as list of list
[[1,2,3], [4,5,6],[7,8,9]]
which has the following slices:
(1,4,7), (1,4,8), (1,5,7), (1,5,8), (1,5,9),
(2,4,7), (2,4,8), (2,5,7), (2,5,8), (2,5,9), (2,6,8), (2,6,9),
(3,5,7), (3,5,8), (3,5,9), (3,6,8), (3,6,9)
Then slice of lowest weight is (1,4,7) which has sum 12.
"""
#####################################################################################
# my solution:
# dfs


class Solution(object):
    def min_slice_cost(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        self.min_cost = 100000
        ans = 0
        for i in range(n):
            self.dfs(matrix, 0, i, m, n, ans)
        return self.min_cost

    def dfs(self, matrix, row, i, m, n, ans):
        ans += matrix[row][i]
        if row == n - 1:
            if ans < self.min_cost:
                self.min_cost = ans
            return
        d = [-1, 0, 1]
        for d_range in d:
            if i + d_range >= 0 and i + d_range < n:
                self.dfs(matrix, row + 1, i + d_range, m, n, ans)


s = Solution()
matrix = \
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
print(s.min_slice_cost(matrix))

#####################################################################################

