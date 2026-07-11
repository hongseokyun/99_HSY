# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        dummy = ListNode()
        curr = dummy
        for num in arr[::-1]:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
        