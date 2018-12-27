# lc 100. Same Tree
    # Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# My solution: construct a string to represent each tree and then check whether the string are the same, for null use "None,"


class Solution(object):
    def is_same_tree(self, p, q):
        return self.helper(p, "") == self.helper(q, "")

    def helper(self, root, tmp):
        if not root:
            tmp += "None,"
        else:
            tmp += str(root.val) + ","
            tmp = self.helper(root.left, tmp)
            tmp = self.helper(root.right, tmp)
        return tmp