class Solution:
    def toHex(self, num: int) -> str:
        if num<0:
            return hex((num + (1 << 32)) % (1 << 32))[2:]
        return hex(num)[2:]
