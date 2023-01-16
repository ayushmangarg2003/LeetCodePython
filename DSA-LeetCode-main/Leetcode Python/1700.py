class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = [len(students) - sum(students), sum(students)]        
        for s in sandwiches:
            if not counts[s]:
                return sum(counts)
            counts[s] -= 1            
        return 0
