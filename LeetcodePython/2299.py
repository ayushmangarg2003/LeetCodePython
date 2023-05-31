class Solution:
    def strongPasswordCheckerII(self, pas: str) -> bool:
        seen = set()
        for i, c in enumerate(pas):
            if i > 0 and c == pas[i - 1]:
                return False
            if c.isupper():
                seen.add('u')
            elif c.islower():
                seen.add('l')
            elif c.isdigit():
                seen.add('d')             
            else:
                seen.add('s')
        return  len(pas) > 7 and len(seen) == 4
