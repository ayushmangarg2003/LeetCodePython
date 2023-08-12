class Codec:
    def serialize(self, root):

        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.right)
                helper(node.left)
            else:
                vals.append('.')
        
        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data):

        def helper():
            val = next(vals)
            if val == '.':
                return None
            node = TreeNode(int(val))
            node.right = helper()
            node.left = helper()
            return node
        
        vals = iter(data.split())
        return helper()
