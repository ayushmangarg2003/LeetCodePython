# Merge Sort

class Solution:
    def middle(self, head):
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left,right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
        curr = head
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left == None:
            curr.next = right
        else:
            curr.next = left
        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        mid = self.middle(head)
        left = head
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)
        head = self.merge(left,right)
        return head
