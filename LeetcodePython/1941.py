class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dum = []
        for i in s:
            dum.append(i)
        sett = set()
        for k,v in Counter(dum).items():
            sett.add(v)
        if len(sett)!=1:
            return 0
        return 1
