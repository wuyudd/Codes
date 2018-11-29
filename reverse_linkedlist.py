# LC 206. Reverse Linked List

# also pay attention to:
#   reverse part array
#   7. Reverse Integer
#   151. Reverse Words in a String
#   344. Reverse String

#####################################################################################
# my solution:
# idea: use linked list pointer


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre

#####################################################################################