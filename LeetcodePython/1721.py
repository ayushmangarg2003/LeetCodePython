class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = b = m = e=  ListNode(0,next=head)
        for i in range(k):
            b = b.next
            m = m.next
        while m:
            m = m.next
            e = e.next
        temp = b.val
        b.val = e.val
        e.val = temp
        return dummy.next
