class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        cur2 = head
        while cur and cur2 and cur2.next:
            cur = cur.next
            cur2 = cur2.next.next
            if cur == cur2:
                return 1
        return 0
