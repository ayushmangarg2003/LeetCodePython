class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = max(amount)
        temp = sum(amount) - 2*max(amount) 
        if temp >0:
            ans+= ((sum(amount) - 2*max(amount))//2)
            if temp%2 != 0:
                ans+=1
        return ans
