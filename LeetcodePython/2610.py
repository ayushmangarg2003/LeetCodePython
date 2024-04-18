class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        ans = []
        for i in nums:
            if freq[i] >= len(ans):
                ans.append([])
            ans[freq[i]].append(i)
            freq[i] += 1
        return ans
