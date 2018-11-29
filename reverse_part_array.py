# reverse part of the array (position m ~ n) in place

# also pay attention to:
#   344. Reverse String
#   7. Reverse Integer
#   151. Reverse Words in a String

# 拓展 可以去做一下leetcode reverse part of linked list


#####################################################################################
# my solution:
# idea: two pointers(kind of like sliding window?)

class Solution(object):
    def reverse_part_array(self, nums, m, n):
        if m > len(nums) or m > n:
            return nums
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        return nums

s = Solution()
nums = [1, 2, 4, 5, 8, 9]
nums1 = []
nums2 = [1]
m = 2
n = 5
print(s.reverse_part_array(nums, m, n))
print(s.reverse_part_array(nums1, m, n))
print(s.reverse_part_array(nums2, m, n))
print(s.reverse_part_array(nums, 5, 2))

#####################################################################################
