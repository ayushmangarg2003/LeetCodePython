# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp1 = curr1 = ListNode(0)
        temp2 = curr2 = ListNode(0)
        curr = head
        while curr:
            if curr.val<x:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
            curr = curr.next
        curr1.next = temp2.next
        return temp1.next 
