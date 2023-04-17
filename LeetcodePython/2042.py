class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        check = 0
        words = s.split()
        for w in words:
            if w.isnumeric():
                if check >= int(w):
                    return False
                else:
                    check = int(w)
        return True
