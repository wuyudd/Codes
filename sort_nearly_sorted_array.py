# Given an array of n elements, where each element is at most k away from its target position
# devise an algorithm that sorts in O(n log k) time.

# My solution: min_heap with size of k

import heapq


class Solution(object):
    def sort_nearly_sorted_array(self, arr, k):
        res = []
        if not arr:
            return res
        k_heap = []
        for ele in arr:
            heapq.heappush(k_heap, ele)
            if len(k_heap) > k:
                res.append(heapq.heappop(k_heap))
        while k_heap:
            res.append(heapq.heappop(k_heap))
        return res


s = Solution()
arr_1 = [6, 5, 3, 2, 8, 10, 9]
k_1 = 3
arr_2 = [10, 9, 8, 7, 4, 70, 60, 50]
k_2 = 4
print(s.sort_nearly_sorted_array(arr_2, k_2))


