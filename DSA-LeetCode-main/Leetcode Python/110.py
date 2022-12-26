class Solution:    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root == None:
                return 0
            return 1 + max(height(root.left) , height(root.right))
        if root == None:
            return True
        lh = height(root.left)
        rh = height(root.right)
        if lh-rh>1 or rh-lh>1:
            return False
        isLeftBal = self.isBalanced(root.left)
        isRightBal = self.isBalanced(root.right)
        if isLeftBal and isRightBal:
            return True
        return False       
