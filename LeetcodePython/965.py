class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        key = root.val
        def search(root, key):
            if not root:
                return True
            return key == root.val and search(root.left, key) and search(root.right, key)
        
        return search(root, key)
