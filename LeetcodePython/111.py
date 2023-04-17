class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        minleft = self.minDepth(root.left)
        minright = self.minDepth(root.right)
        if minleft<=0:
            return 1+minright
        if minright<=0:
            return 1+minleft
        return 1+ min(minright , minleft) 
