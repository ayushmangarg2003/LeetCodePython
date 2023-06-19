class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [float(-inf),float(-inf)]
        for i in mat:
            if ans[1] < i.count(1):
                ans[0] = mat.index(i)
                ans[1] = i.count(1)
        return ans
