class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(x, y):
            while(y):
                x, y = y, x % y
            return abs(x)
        curr = head
        if not head.next:
            return head
        while curr and curr.next:
            temp = ListNode(gcd(curr.val, curr.next.val))
            temp.next = curr.next
            curr.next = temp
            curr = curr.next.next
        return head
