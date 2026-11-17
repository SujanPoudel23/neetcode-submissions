"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def DFS(self, node, mappings):
        newNode = Node()
        newNode.val = node.val
        newNode.neighbors = []
        mappings[newNode.val] = newNode

        for neighbor in node.neighbors:
            if neighbor.val not in mappings:
                mappings[neighbor.val] = None
                newN = self.DFS(neighbor, mappings)
                mappings[neighbor.val] = newN

                newNode.neighbors.append(newN)
            else:
                newNode.neighbors.append(mappings[neighbor.val])

        return newNode


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mappings = {}

        if node is None:
            return node

        root = self.DFS(node, mappings)
        
        return root

        