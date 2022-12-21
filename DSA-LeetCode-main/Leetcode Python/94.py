class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root:
            res += self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        return res
