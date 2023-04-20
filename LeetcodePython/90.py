class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path, res):
            if path not in res:
                res.append(path)
            for i in range(start, len(nums)):
                dfs(i+1, path + [nums[i]], res)
        nums.sort()
        res = []
        dfs(0, [], res)
        return res
