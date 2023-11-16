# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        if not head.next:
            return head

        prev = head
        current = head.next

        while current:
            if current.val == prev.val:
                current = current.next
                prev.next = current
            else:
                # Just advance
                prev = prev.next
                current = current.next

        return head