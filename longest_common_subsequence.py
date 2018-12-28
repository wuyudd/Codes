# Longest Common Subsequence
    # Examples:
    # LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
    # LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
# My solution: DP


class Solution(object):
    def longest_common_subsequence(self, str_1, str_2):
        m = len(str_1)
        n = len(str_2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        common = []
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str_1[i-1] == str_2[j-1]:
                    common.append(str_1[i-1])
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n], common


s = Solution()
str_1 = "ABCDGH"
str_2 = "AEDFHR"
common_cnt, common = s.longest_common_subsequence(str_1, str_2)
print(common_cnt)
print(common)