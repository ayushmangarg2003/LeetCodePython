class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in nums2:
            if i in nums1:
                nums1.remove(i)
            elif i not in nums1:
                nums2.remove(i)
        return nums2
           
