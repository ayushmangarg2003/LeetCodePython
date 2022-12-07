class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        sta = 0
        end = len(nums) - 1
        while sta<=end:
            mid = (sta + end)//2
            midnum = nums[mid]
            if midnum == target:
                return nums.index(midnum)
            elif midnum > target:
                end = mid-1
            else:
                sta = mid+1
