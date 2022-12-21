class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        temp = list(set(temp))
        temp.sort()
        dummy = curr = ListNode(0)
        for i in temp:
            curr.next = ListNode(i)
            curr = curr.next
        return dummy.next
