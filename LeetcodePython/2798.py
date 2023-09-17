class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        for i in range(len(hours)):
            if hours[i]>=target:
                return len(hours)-i
        return 0
