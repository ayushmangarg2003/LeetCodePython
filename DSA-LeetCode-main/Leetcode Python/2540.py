class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = set(nums1), set(nums2)
        common = sorted(list(nums1 & nums2))
        return -1 if not len(common) else common[0]
        
