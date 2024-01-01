class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        traversal = s.split("-")
        root = TreeNode(int(traversal[0]))
        curr = root
        for i in traversal[1:]:
            if i == "":
                curr = curr.right if curr.right else curr.left
            else:
                if not curr.left:
                    curr.left = TreeNode(int(i))
                else:
                    curr.right = TreeNode(int(i))
                curr = root    #after every insertion we are moving curr back to root so that it can navigate again
        return root
