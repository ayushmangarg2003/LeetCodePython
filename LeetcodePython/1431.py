class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
         ans =[]
         maxc = max(candies)
         for i in range(len(candies)):
            if candies[i]+extraCandies >= maxc :
                ans.append(1)
            else:
                ans.append(0)
         return ans
