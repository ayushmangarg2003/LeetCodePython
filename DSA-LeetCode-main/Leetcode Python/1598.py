class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for i in logs:
            if i == '../':
                if ans>0:
                    ans-=1
                else:
                    continue
            elif i == './':
                continue
            else:
                ans+=1
        if ans > 0:
            return ans
        return 0
