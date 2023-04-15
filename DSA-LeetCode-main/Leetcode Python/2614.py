class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        dummy = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i == j or i+j == len(nums)-1:
                    dummy.append(nums[i][j])
        for i in sorted(dummy,reverse=True):
            if self.isPrime(i) and i!=1:
                return i
        return 0

    def isPrime(self, n):
        for i in range(2,n):
            if (n%i) == 0:
                return False
        return True
