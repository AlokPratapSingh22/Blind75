"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Examples

Example 1:
Input: n = 5 edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true.

Example 2:
Input: n = 5 edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false.
"""

def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
    adj = {i:[] for i in range(n)}

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    vis = set()

    q = [(0, -1)]

    # the traversal can be done using dfs as well

    while q:
        u, par = q.pop(0)
        vis.add(u)

        for v in adj[u]:
            if par==v: continue

            if v in vis: return False
            
            q.append((v,u))
    
    return len(vis) == n