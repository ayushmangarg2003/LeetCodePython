class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def isNotPalindrom(num):
            if str(num)[::-1] == str(num):
                return False
            return True
        def convert(number, base):
            digits = '0123456789abcdefghijklmnopqrstuvwxyz'
            result = ''
            while number > 0:
                result = digits[number % base] + result
                number //= base
            return result
            
        for i in range(2,n-1):
            if isNotPalindrom(convert(n, i)):
                return False
        return True
