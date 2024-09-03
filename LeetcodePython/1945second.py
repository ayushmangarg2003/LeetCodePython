class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''
        for i in s:
            number+= str(ord(i) - ord('a') + 1)
        while k > 0:
            temp = 0
            for i in number:
                temp += int(i)
            number = str(temp)
            k-=1
        return int(number)
