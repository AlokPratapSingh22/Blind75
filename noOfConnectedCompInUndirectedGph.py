"""
Given a graph with V vertices. Find the number of connected components.

Example 1:
Input:
{   1: [3],
    3: [1],
    2: []
}, 3
Output:
2
Explanation: The graph clearly has 2 Provinces. 
"""

def countComponents(adj, n):
    vis = set()
    cnt = 0

    for i in range(n):
        # entry (node, parent)
        if i in vis: continue

        q = [(i, -1)]

        while q:
            u, par = q.pop(0)
            vis.add(u)
            for v in adj[u]:
                if v == par or v in vis: continue
                q.append((v, u))
        
        cnt+=1

    return cnt