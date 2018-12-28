# lc 105. Construct Binary Tree from Preorder and Inorder Traversal

# My solution:
#   Preorder[0] is the root
#   find the root position r_p in Inorder
#   Inorder[:r_p] is for left subtree, Inorder[r_p:] is for right subtree
#   recursively until construct successfully


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def construct_BT_pre_in(self, preorder, inorder):

        def dfs(p_begin, p_end, i_beign, i_end):
            if p_begin >= p_end:
                return None # end condition
            if p_begin + 1 == p_end:
                return TreeNode(preorder[p_begin])
            root_idx = inorder.index(preorder[p_begin])
            rng = root_idx - i_beign

            ans = TreeNode(preorder[p_begin])
            ans.left = dfs(p_begin+1, p_begin+1+rng, i_beign, i_beign+rng)
            ans.right = dfs(p_begin+1+rng, p_end, i_beign+rng+1, i_end)
            return ans

        return dfs(0, len(preorder), 0, len(inorder))
