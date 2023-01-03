class Solution(object):
    
    def reverse(self,arr,a,b):
        while(a<=b):
            arr[a],arr[b]=arr[b],arr[a]
            a+=1
            b-=1
            
    def rotate(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        k = k%n
        self.reverse(arr,n-k,n-1)
        self.reverse(arr,0,n-k-1)
        self.reverse(arr,0,n-1)
