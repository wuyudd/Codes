# lc 50. Pow(x, n)

# My solution: half -> O(log(n))


class Solution(object):
    def my_pow(self, x, n):
        if n < 0:
            n = -n
            x = 1/x
        elif n == 0:
            return 1

        curr = x
        res = 1
        while n:
            if n % 2:
                res *= curr
                n -= 1
            else:
                curr = curr ** 2
                n //= 2
        return res


s = Solution()
x = 3
n = 4
print(s.my_pow(x, n))