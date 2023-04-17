class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        summ = 0
        for i in range(len(arr)):
            ans = arr[i]+arr[len(arr)-i-1]
            summ = max(ans, summ)
        return summ
