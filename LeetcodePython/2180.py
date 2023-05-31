class Solution:
    def countEven(self, num: int) -> int:
        sum = 0
        n = num
        while n > 0:
            sum+= n%10
            n = n//10
        if sum%2==0:
            return int(num/2)
        elif num%2 ==0:
            return num//2 -1
        else:
            return (num+1)//2  -1
