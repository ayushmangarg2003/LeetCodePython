class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out =[]
        for i in nums1:
            for j in nums2:
                if i==j:
                    out.append(i)
        out2 = set(out)
        return out2
