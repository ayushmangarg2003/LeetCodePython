class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = []
        for k,v in count.items():
            if v>2:
                while v!=2:
                    nums.remove(k)
                    v-=1
        return len(nums)
