# LC 5. Longest Palindromic Substring

# also pay attention to subarray problems:
#   is palindrome

#####################################################################################
# my solution:
# idea: use two pointers to check for odd length and even length palindrome separately

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            tmp = self.helper(i, i, s)
            if len(res) < len(tmp):
                res = tmp
            tmp = self.helper(i, i + 1, s)
            if len(res) < len(tmp):
                res = tmp
        return res

    def helper(self, l, r, s):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l + 1:r]

#####################################################################################