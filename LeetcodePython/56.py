class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort()
        i = 0
        while i<len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                intervals.append([intervals[i][0],intervals[i][1]])
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.sort()

            elif(intervals[i][1]>=intervals[i+1][0] and intervals[i][1]<intervals[i+1][1]):
                intervals.append([intervals[i][0],intervals[i+1][1]])
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.sort()
            else:
                i+=1
        return intervals
