class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        count_of_3s = n // 3
        remainder = n % 3
        if remainder == 0:
            return 3 ** count_of_3s
        elif remainder == 1:
            return 3 ** (count_of_3s - 1) * 4
        else:  
            return 3 ** count_of_3s * 2
#basic observation that is we break a number into as many 3 as possible then it will give maximum product so I did the same in code above
