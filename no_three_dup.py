# 寻找一个用a和b组成的字符串，其中a出现A次，b出现B次，要求不存在三个连续的相同字符。Input两个整数 A和B，输出任何一个满足条件的，比如A是5 B是3，那么输出可以是aabaabba 也可以是 aabbaaba
    # if A = B, abab
    # if A > B and A < B*2, abab -> nA - k = 2 (nB - k) -> aab
    # if A = B*2, aab
    # if A > B * 2, no solution


class Solution(object):
    def no_three_dups(self, A, B):
        res = ""
        is_reverse = 0
        if A < B:
            A, B = B, A
            is_reverse = 1
        if A == B:
            res = "ab" * A
        elif B < A < 2 * B:
            k1 = 2 * B - A
            k2 = B - (2 * B - A)
            res = "ab" * k1 + "aab" * k2
        elif A == 2 * B:
            res = "aab" * B

        if is_reverse:
            res_lst = list(res)
            for i in range(len(res_lst)):
                res_lst[i] = "a" if res_lst[i] == "b" else "b"
            res = "".join(res_lst)
        return res


s = Solution()
A, B = 3, 5
print(s.no_three_dups(A, B))