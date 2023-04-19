class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        num = (len(arr))//20
        summ = sum(arr[num:len(arr)-num])/(len(arr)-(2*num))
        return summ
