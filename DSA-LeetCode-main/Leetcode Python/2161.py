class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        for i in nums:
            if i<pivot:
                ans.append(i)
        for i in nums:
            if i == pivot:
                ans.append(i)
        for i in nums:
            if i>pivot:
                ans.append(i)
        return ans
