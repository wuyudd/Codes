# lc 72. Edit Distance

# My solution: DP
# ref: https://www.dreamxu.com/books/dsa/dp/edit-distance.html

class Solution(object):
    def min_dist(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[-1] * n for _ in range(m)]

        def helper(i, j):
            if i < 0:
                return j + 1
            elif j < 0:
                return i + 1
            elif dp[i][j] == -1:
                if word1[i] == word2[j]:
                    dp[i][j] = helper(i-1, j-1)
                else:
                    dp[i][j] = 1 + min(helper(i-1, j-1), helper(i-1, j), helper(i, j-1))
            return dp[i][j]

        return helper(m-1, n-1)
