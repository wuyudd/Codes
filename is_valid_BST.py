# 98. Validate Binary Search Tree

# also pay attention to subarray problems:
#

#####################################################################################
# my solution:
# idea: recursively check left and right value


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, root, low, high):
        if root is None:
            return True
        if not low < root.val < high:
            return False
        left = self.helper(root.left, low, root.val)
        right = self.helper(root.right, root.val, high)
        return left and right

#####################################################################################