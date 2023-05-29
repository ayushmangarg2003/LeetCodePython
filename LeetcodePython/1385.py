class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in arr1:
            temp = 0
            for j in arr2:
                if abs(i-j) <=d:
                    temp+=1
            if temp ==0:
                ans+=1
        return ans

      
