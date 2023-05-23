class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:
            ne=n//2
        else:
            ne=(n+1)//2   
        return (pow(4,n//2,10**9+7)*pow(5,ne,10**9+7))%(10**9+7)
