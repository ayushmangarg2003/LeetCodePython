# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        point = ans = ListNode(0)
        temp = 0
        while curr.next:
            curr = curr.next
            temp += curr.val
            if curr.val == 0:
                point.next = ListNode(temp)
                temp = 0
                point = point.next
        return ans.next

