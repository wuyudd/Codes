# 108. Convert Sorted Array to Binary Search Tree

# also pay attention to subarray problems:
#

#####################################################################################
# my solution:
# idea: recursive, mid as root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sorted_array_to_BST(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_BST(nums[:mid])
        root.right = self.sorted_array_to_BST(nums[mid+1:])
        return root

#####################################################################################