class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes = [sorted(x) for x in dominoes]
        ans = []
        visited = []
        for i in dominoes:
            if i not in visited:
                visited.append(i)
                if dominoes.count(i)>1:
                    ans.append(sum(range(dominoes.count(i))))
        return sum(ans)
