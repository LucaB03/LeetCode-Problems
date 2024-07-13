# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head.next
        head = ListNode(head.val)
        while current:
            new = ListNode(current.val)
            new.next = head
            head = new
            current = current.next
        return head
            