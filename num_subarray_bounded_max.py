# LC 795. Number of Subarrays with Bounded Maximum

# also pay attention to subarray problems:
#   713. Subarray Product Less Than K
#   53. Maximum Subarray
#   same subsum

#####################################################################################
# my solution:
# idea: two pointers(kind of like sliding window?)

class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        l = r = -1
        ans = 0
        for i in range(len(A)):
            if A[i] > R:
                l = i
            if A[i] >= L:
                r = i
            ans += r - l
        return ans


s = Solution()
A = [2, 1, 4, 3]
L = 2
R = 3
print(s.numSubarrayBoundedMax(A, L, R))

#####################################################################################
