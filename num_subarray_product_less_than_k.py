# LC 713. Subarray Product Less Than K

# also pay attention to subarray problems:
#   795. Number of Subarrays with Bounded Maximum
#   53. Maximum Subarray
#   same subsum

#####################################################################################
# my solution:
# idea: sliding window

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0

        prod = 1
        l = ans = 0

        for r, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[l]
                l += 1
            ans += r - l + 1

        return ans

s = Solution()
nums = [10, 5, 2, 6]
k = 100
print(s.numSubarrayProductLessThanK(nums, k))

#####################################################################################
