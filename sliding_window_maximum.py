# lc 239. Sliding Window Maximum

# My solution: use deque which can add/delete element from left
#   solution 1:
import collections


class Solution(object):
    def max_sliding_window(self, nums, k):
        res = []
        if len(nums) < k or k == 0:
            return res
        dq = collections.deque(nums[:k])
        curr_max = max(dq)
        res.append(curr_max)
        for i in range(k, len(nums)):
            pp = dq.popleft()
            dq.append(nums[i])
            if pp == curr_max:
                curr_max = max(dq)
            elif nums[i] > curr_max:
                curr_max = nums[i]
            res.append(curr_max)
        return res


#   solution 2:
class Solution_2(object):
    def max_sliding_window_2(self, nums, k):
        res = []
        if not nums or k == 0:
            return res

        dq = collections.deque()
        for i in range(k):
            while dq:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break
            dq.append(i)

        for i in range(k, len(nums)):
            res.append(nums[dq[0]])
            if dq[0] < i - k + 1:
                dq.popleft()
            while dq:
                if nums[i] > nums[dq[-1]]:
                    dq.pop()
                else:
                    break
            dq.append(i)
        res.append(nums[dq[0]])

        return res

