# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        while p2 is not None:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
        head.next = None
        return p1
        
