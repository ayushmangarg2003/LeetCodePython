class Solution:
    def getIntersectionNode(self, headA: ListNode(), headB: ListNode()) -> Optional[ListNode]:
        curr1 , curr2 = headA , headB 
        a , b = 0 , 0
        while curr1:
            a+=1
            curr1 = curr1.next
        while curr2:
            b+=1
            curr2 = curr2.next
        if a > b:
            currL = headA
            diff = a-b
            currS = headB
        else:
            currL = headB
            diff = b-a
            currS = headA
        i = 0
        while i < diff:
            i+=1
            currL = currL.next
        while currL != currS:
            currL = currL.next
            currS = currS.next
        return currL
        
        
         
