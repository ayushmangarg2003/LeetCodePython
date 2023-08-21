class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        l,r=height[left],height[right]
        ans=0
        while left<right:
            l,r=max(l,height[left]),max(r,height[right])
            if l<=r:
                ans+=l-height[left]
                left+=1
            else:
                ans+=r-height[right]
                right-=1
        return ans
