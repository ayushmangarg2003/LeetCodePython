class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkAP(arr):
            temp = set()
            arr.sort()
            for i in range(len(arr)-1):
                temp.add(arr[i+1] - arr[i])
            return len(temp) == 1
        
        ans = [False] * len(l)
        for i in range(len(l)):
            ans[i] = checkAP(nums[l[i]:r[i]+1])
        return ans
