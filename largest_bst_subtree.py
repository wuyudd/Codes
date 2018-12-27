# lc 333 largest BST subtree
    # Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

# My solution: recursively from bottom to top, check whether the subtree from this node to the leaf is BST or not

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return res[2]

    def helper(self, node):
        if not node:
            return float('inf'), float('-inf'), 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if node.val > left[1] and node.val < right[0]:
            return min(node.val, left[0]), max(node.val, right[1]), left[2]+right[2]+1
        return float('-inf'), float('inf'), max(left[2], right[2])