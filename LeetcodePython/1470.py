class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        i=0
        n2 = n
        while i<n2:
            ans.append(nums[i])
            i+=1
            ans.append(nums[n])
            n+=1
        return ans
