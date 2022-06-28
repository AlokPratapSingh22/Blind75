"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

For example,
Given the following words in dictionary,

[
"wrt",
"wrf",
"er",
"ett",
"rftt"
]
The correct order is: "wertf".
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
"""
from collections import defaultdict

def alienDictonary(words: list[str]) -> str:
    edges = set()

    for i in range(len(words)-1):
        if words[i] == words[i+1]: continue

        l1 = len(words[i])
        l2 = len(words[i+1])

        for j in range(min(l1,l2)):
            if words[i][j] != words[i+1][j]:
                edges.add((words[i][j], words[i+1][j]))
                break
            
    adj = {c:set() for w in words for c in w}
    indegree = {k:0 for k in adj}
    
    for u,v in edges:
        adj[u].add(v)
        indegree[v]+=1
    
    q = []
    for key in indegree:
        if indegree[key] == 0:
            q.append(key)

    res = ""
    while q:
        u = q.pop(0)
        res += u
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    
    return res

print(alienDictonary(['zy', 'zx'])) # zyx/ yxz
print(alienDictonary(["caa", "aaa", "aab"])) # cab