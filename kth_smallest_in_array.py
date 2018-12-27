# kth largest(or smallest) elements in an array
    # use min_heap and for kth smallest elements == len(nums) - k largest

# My solution: min_heap
import heapq


class Solution(object):
    def kth_smallest(self, nums, k):
        if not nums:
            return 0
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > len(nums)-k+1:
                heapq.heappop(heap)
        return heap[0]


s = Solution()
nums = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(s.kth_smallest(nums, k))



