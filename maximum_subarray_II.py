# find out two non-overlapping subarrays, which are both contiguous has the largest sum

# My solution: use DP which is used in maximum_subarray.py for left and right subarray respectively


class Solution(object):
    def max_two_subarray(self, arr):
        max_sum = 0
        for i in range(len(arr)):
            sum_1 = self.max_subarray(arr[:i])
            sum_2 = self.max_subarray(arr[i:])
            max_sum = max(max_sum, sum_1 + sum_2)
        return max_sum

    def max_subarray(self, arr):
        if not arr:
            return 0
        max_ending_here = max_sum = arr[0]
        for i in range(1, len(arr)):
            max_ending_here = max(max_ending_here + arr[i], arr[i])
            max_sum = max(max_sum, max_ending_here)
        return max_sum


s = Solution()
arr = [1, 3, -1, 2, -1, 2]
print(s.max_two_subarray(arr))