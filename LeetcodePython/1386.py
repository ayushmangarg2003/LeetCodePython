from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedrows = defaultdict(set)
        for i, j in reservedSeats:
            if 2 <= j <= 9:
                reservedrows[i].add(j)
        
        result = 2*n
        for i in reservedrows.keys():
            reserved = reservedrows[i]
            if not {4,5,6,7} & reserved and {2,3,8,9} & reserved:
                result -= 1
            else:
                if {2,3,4,5} & reserved:
                    result -= 1
                if {6,7,8,9} & reserved:
                    result -= 1
        return result
