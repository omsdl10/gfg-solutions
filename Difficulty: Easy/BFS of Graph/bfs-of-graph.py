class Solution:
    def bfs(self, adj):
        # code here
        n=len(adj)
        visited=[False]*n
        res=[]
        q=deque()
        src=0
        q.append(src)
        while q:
            node=q.popleft()
            res.append(node)
            visited[node]=True
            for i in adj[node]:
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
        return res