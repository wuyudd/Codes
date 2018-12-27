# lc 53. Maximum Subarray
    # Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# My solution: DP


class Solution(object):
    def max_subarray(self, nums):
        if not nums:
            return 0
        max_ending_here = max_sum = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_sum = max(max_sum, max_ending_here)
        return max_sum


s = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(s.max_subarray(nums))
