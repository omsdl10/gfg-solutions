def reldfs(adj,res,i,visited):
    visited[i]=True
    res.append(i)
    for j in adj[i]:
        if not visited[j]:
            reldfs(adj,res,j,visited)
class Solution:
    def dfs(self, adj):
        # code here
        visited=[False]*len(adj)
        res=[]
        reldfs(adj,res,0,visited)
        return res