# Calculate the length of a linked list, which is represented by an array. Each element in the array represents the index of next element
# if the element is -1, the array ends.


class Solution(object):
    def len_of_linked_list(self, array):
        i = 0
        cnt = 0
        while array[i] != -1:
            i = array[i]
            cnt += 1
        return cnt


s = Solution()
array = [2, 3, 1, 4, -1, 8]
print(s.len_of_linked_list(array))


