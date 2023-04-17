class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy
        for i in lists:
            ptr.next = i
            while ptr.next:
                ptr = ptr.next
        dummy = dummy.next
        curr = dummy
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr.sort()
        cur = dummy2 = ListNode(0)
        for e in arr:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy2.next





