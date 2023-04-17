class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        cur = head
        while cur:
            temp.append(cur.val)
            cur = cur.next
        c = Counter(temp)
        temp = [k for k,v in c.items() if v==1] 
        dummy  = cur = ListNode()
        for i in temp:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next 
