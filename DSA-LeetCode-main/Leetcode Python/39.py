class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []
        res = []
        for i in range(len(candidates)):
            if candidates[i]==target:
                res.append([target])
            else:
                for prev in self.combinationSum(candidates[i:],target-candidates[i]):
                    res.append([candidates[i]] + prev)
        return res
