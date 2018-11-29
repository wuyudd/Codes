# LC 151. Reverse Words in a String

# also pay attention to:
#   reverse part array
#   7. Reverse Integer
#   344. Reverse String

#####################################################################################
# my solution:
# idea: two pointers

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        l, r = 0, len(words) - 1

        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1

        return " ".join(words)

#####################################################################################
