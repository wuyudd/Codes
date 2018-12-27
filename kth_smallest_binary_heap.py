# Find kth smallest element from a binary heap
    # We have an n-node binary heap which contains n distinct items (smallest item at the root).
    # For a k<=n, find a O(klogk) time algorithm to select kth smallest element from the heap.

# My solution: O(klogk)
    # 1-create and maintain a min_heap k_heap with size of k, initialize it with root of original binary heap
    # 2-delete the root ele in the k_heap and add in the two children of the root
    # 3-iterate it for k-1 times and the current root of the k_heap is what we need = kth smallest element from a binary heap

# Related problems:
    # lc 703. Kth Largest Element in a Stream

import heapq


class Solution(object):
    def kth_smallest_ele(self, arr, k):
        if not arr:
            return 0
        k_heap = [(arr[0], 0)]
        for i in range(k-1):
            curr_root = heapq.heappop(k_heap)
            curr_idx = curr_root[1]
            if 2*curr_idx+1 < len(arr):
                heapq.heappush(k_heap, (arr[2*curr_idx+1], 2*curr_idx+1))
            else:
                heapq.heappush(k_heap, (float('inf'), float('inf')))
            if 2*curr_idx+2 < len(arr):
                heapq.heappush(k_heap, (arr[2*curr_idx+2], 2*curr_idx+2))
            else:
                heapq.heappush(k_heap, (float('inf'), float('inf')))
        return heapq.heappop(k_heap)[0]


s = Solution()
arr_1 = [2, 3, 1, 6, 8, 9, 5, 7, 11, 13, 15]
heapq.heapify(arr_1)
arr_2 = []
k = 9
print(s.kth_smallest_ele(arr_1, k))