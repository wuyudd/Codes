# LC 53. Maximum Subarray

# also pay attention to subarray problems:
#   713. Subarray Product Less Than K
#   795. Number of Subarrays with Bounded Maximum
#   same subsum
#####################################################################################
# my solution:
# idea: dp

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

