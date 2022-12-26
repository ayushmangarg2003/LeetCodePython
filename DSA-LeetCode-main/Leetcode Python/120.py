class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path = [0]*(len(triangle)+1)
        for i in triangle[::-1]:
            for j , n in enumerate(i):
                path[j] = n + min(path[j] , path[j+1])
        return path[0]
            
