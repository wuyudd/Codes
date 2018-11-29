# LC 344. Reverse String

# also pay attention to:
#   reverse part array
#   7. Reverse Integer
#   151. Reverse Words in a String
#   206. Reverse Linked List
#####################################################################################
# my solution:
# idea: s[::-1] / reversed() / two pointers

# 1: s[::-1]
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


# 2 reversed()
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(reversed(s))


# 3 two pointers
#   * string item cannot get assignment, so we need to transfer the string into list and then use two pointers
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        l, r = 0, len(s) - 1
        s_lst = list(s)
        while l < r:
            s_lst[l], s_lst[r] = s_lst[r], s_lst[l]
            l += 1
            r -= 1
        return "".join(s_lst)

#####################################################################################
