class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr2 = curr = ListNode(0,next = head)
        count = 0
        while curr:
            curr = curr.next
            count+=1
        if count%2==0:
            count = count//2 - 1
        else:
            count = count//2
        while count!=0:
            count-=1
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return dummy.next
