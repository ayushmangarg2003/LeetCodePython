class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxx=0
        res=float("inf")
        for i in divisors:
            temp=0
            for j in nums:
                if j%i==0:
                    temp+=1
            if temp>maxx:
                maxx=temp
                res=i
            elif temp==maxx:
                maxx=temp
                res=min(res,i)      
        return res
            
        
