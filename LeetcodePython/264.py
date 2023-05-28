class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        u2 , u3 , u5 = 0 , 0 , 0
        while len(ugly)<n:
            next_ugly = min(ugly[u2]*2 , ugly[u3]*3 , ugly[u5]*5)
            ugly.append(next_ugly)
            if next_ugly == ugly[u2]*2:
                u2+=1
            if next_ugly == ugly[u3]*3:
                u3+=1
            if next_ugly == ugly[u5]*5:
                u5+=1
        return ugly[-1]
