# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        while head is not None:
            vals.append(head.val)
            head = head.next

        dummy = ListNode()
        current = dummy

        for val in vals[::-1]:
            current.next = ListNode(val)
            current = current.next

        return dummy.next