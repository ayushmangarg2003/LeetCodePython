class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            if i in nums2 or i in nums3:
                ans.append(i)
        for i in nums2:
            if i in nums3 or i in nums1:
                ans.append(i)
        for i in nums3:
            if i in nums1 or i in nums2:
                ans.append(i)
        return set(ans)
