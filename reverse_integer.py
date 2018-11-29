# LC 7. Reverse Integer

# also pay attention to:
#   reverse part array
#   344. Reverse String
#   151. Reverse Words in a String

#####################################################################################
# my solution:
# idea: int() str() / digit // %


# 1: use str() and int() and is_neg
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x < 0:
            is_neg = True

        reversed_s = int(str(abs(x))[::-1])

        if is_neg:
            reversed_s = -1 * reversed_s
            reversed_s = reversed_s * (reversed_s >= -2 ** 31)
        else:
            reversed_s = reversed_s * (reversed_s < 2 ** 31)

        return reversed_s


# 2: use digit to compose number
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = False
        if x < 0:
            is_neg = True

        x = abs(x)
        res = []
        # this part is to reverse the digits composing the number
        while x // 10 > 0:
            res.append(x % 10)
            x //= 10
        res.append(x % 10)

        final = 0
        for digit in res:
            final = final * 10 + digit

        if is_neg:
            final = -final * (-final >= -2 ** 31)
        else:
            final = final * (final <= 2 ** 31 - 1)

        return final

#####################################################################################