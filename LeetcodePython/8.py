class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ['-', '+']:
            s = s[1:] 

        res = 0
        for i in s:
            if not i.isdigit():
                break
            res = res * 10 + int(i)
            if res * sign >= 2**31 - 1:
                return 2**31 - 1
            if res * sign <= -2**31:
                return -2**31
        return res * sign
