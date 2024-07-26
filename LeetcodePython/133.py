from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
            
        if node:
            return clone(node)
        else:
            return None
