class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        dum = ""
        for i in nums:
            dum+=str(i)
        for i in dum:
            ans.append(int(i))
        return ans
