# given an array consisting of only positive integers.
# Separate the array into two contingous parts 1 and 2, let sum of part 1 equals sum of part 2.
# give the index of the element that separates these two parts. Assume only one unique answer.
# for example：[1,2,3], returns 1; [1,2,3,4,5,5] =>	[1,2,3,4] [5,5]

# also pay attention to subarray problems:
#   713. Subarray Product Less Than K
#   795. Number of Subarrays with Bounded Maximum
#   53. Maximum Subarray

#####################################################################################
# my solution:
# idea: two pointers

class Solution(object):
    def same_sum(self, nums):
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        sum_1 = sum_2 = 0
        while l < r:
            if sum_1 < sum_2:
                sum_1 += nums[l]
                l += 1
            else:
                sum_2 += nums[r]
                r -= 1
        return l

s = Solution()
nums1 = [1, 2, 3]
nums2 = [1, 2, 3, 4, 5, 5]
nums3 = []
nums4 = [1, 2, 3, 3, 2, 1]
nums5 = [2, 1, 5, 5, 2, 1]

print(s.same_sum(nums1))
print(s.same_sum(nums2))
print(s.same_sum(nums3))
print(s.same_sum(nums4))
print(s.same_sum(nums5))

#####################################################################################



