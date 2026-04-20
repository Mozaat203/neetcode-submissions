from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 1. Guard Clause for empty graph
        if not node:
            return None

        # 2. Initialization: Registry and Queue
        oldToNew = {}
        queue = deque([node])
        
        # Pre-seed the first node
        oldToNew[node] = Node(node.val)

        # 3. BFS Traversal Engine
        while queue:
            curr = queue.popleft()
            
            # Look at all neighbors of the ORIGINAL node
            for neighbor in curr.neighbors:
                # If neighbor hasn't been mirrored yet
                if neighbor not in oldToNew:
                    # Create the mirror/clone
                    oldToNew[neighbor] = Node(neighbor.val)
                    # Add original neighbor to queue to visit its own neighbors
                    queue.append(neighbor)
                
                # LINKAGE: Connect the mirror of 'curr' to the mirror of 'neighbor'
                # This ensures a Deep Copy (New -> New)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]