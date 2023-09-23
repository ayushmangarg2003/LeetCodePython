class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head
        curr2 = head
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 == curr2:
                curr1 = head
                while curr1 != curr2:
                    curr1 = curr1.next
                    curr2 = curr2.next
                return curr1
        return None
