class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {'2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'}
        ans = [""]
        if not digits:return []
        for i in digits:
            tmp = []
            for v in dict1[i]:
                for o in ans:
                    tmp.append(o+v)
            ans = tmp
        return ans
