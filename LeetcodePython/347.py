class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        unique = []
        freq = []
        for i in nums:
            if i not in unique:
                unique.append(i)
                freq.append(nums.count(i))
        for i in range(k):
            m = max(freq)
            j = freq.index(m)
            ans.append(unique[j])
            freq[j]=-1
        return ans
