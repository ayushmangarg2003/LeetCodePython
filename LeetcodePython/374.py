class Solution:
    def guessNumber(self, n: int) -> int:
        low,high=1,n
        mid=0
        while low<high:
            mid=low+(high-low)/2
            mid=int(mid)
            if guess(mid)==-1:
                high=mid-1
            elif guess(mid)==1:
                low=mid+1
            else:
                return mid
        return low
