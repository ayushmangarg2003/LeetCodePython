class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = s = f = ListNode(0,next=head)
        for i in range(n):
            f = f.next
        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return dummy.next
