class Solution:
    def countPoints(self, rings: str) -> int:
        ans = 0
        for i in range(10):
            if f"R{i}" in rings and f"G{i}" in rings and f"B{i}" in rings:
                ans+=1
        return ans
