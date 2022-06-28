"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

def cloneGraph(node: 'Node') -> 'Node':
    if not node: return None
    
    new_node = Node(node.val, [])
    
    nmap = {
        node: new_node
    }
    
    q = [node]
    
    while q:
        u= q.pop(0)            
        
        for v in u.neighbors:                
                                
            if v not in nmap:
                nmap[v] = Node(v.val, [])
                q.append(v)
            nmap[u].neighbors.append(nmap[v])                
    
    return new_node