class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        list1 = []
        for i in nums :
            if i in list1 :
                return i
            else :
                list1.append(i)
