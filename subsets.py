# LC 78. Subsets

# also pay attention to:
#
#####################################################################################
# my solution:
# idea: for + recursive


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, start, path, result):
        result.append(path)
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            self.helper(nums, i + 1, path + [nums[i]], result)


s = Solution()
nums = [1, 2, 3]
print(s.subsets(nums))

#####################################################################################
