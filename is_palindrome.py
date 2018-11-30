# check whether the given string is a palindrome, ignore all the non-alphabet elements

# also pay attention to subarray problems:
#   5. Longest Palindromic Substring

#####################################################################################
# my solution:
# idea: two pointers

if __name__ == '__main__':
    class Solution(object):
        def palindrome(self, S):
            if not S:
                return True
            l, r = 0, len(S) - 1
            while l < r:
                if S[l].isalpha():
                    if S[r].isalpha():
                        if S[l] == S[r]:
                            l += 1
                            r -= 1
                        else:
                            return False
                    else:
                        r -= 1
                else:
                    l += 1
            return True

    s = Solution()
    S = "ab@dqu*dba"
    S1 = ""
    S2 = " ,"
    print(s.palindrome(S))
    print(s.palindrome(S1))
    print(s.palindrome(S2))

#####################################################################################