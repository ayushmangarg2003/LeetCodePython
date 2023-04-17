# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        temp = temp[::-1]
        dummy = curr = ListNode(0)
        for i in temp:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
