class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums1 = []
        target1 = []
        nums2 = []
        target2 = []
        nums.sort()
        target.sort()
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums1.append(nums[i])
            else:
                nums2.append(nums[i])
            if target[i]%2==0:
                target1.append(target[i])
            else:
                target2.append(target[i])
        inc = 0
        for i in range(len(nums1)):
            if nums1[i]<target1[i]:
                inc+=((target1[i]-nums1[i])//2) 
                
        for i in range(len(nums2)):
            if nums2[i]<target2[i]:
                inc+=((target2[i]-nums2[i])//2)
        return inc
      
