class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        curr = 0
        next = 0
        while curr < len(boxes):
            while next < len(boxes):
                ans[curr]+= abs(next-curr) * int(boxes[next])
                next+=1
            curr+=1
            next = 0
        return ans


# Alternate Solution with less memory
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                ans[i] += int(boxes[j]) * (abs(j-i))            
        return ans
