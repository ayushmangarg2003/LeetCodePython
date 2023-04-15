class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        tail = head
        length = 1
        while tail.next:
            tail = tail.next
            length+=1
        k = k % length
        if k==0:
            return head
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        new = curr.next
        curr.next = None
        tail.next = head
        return new
        
