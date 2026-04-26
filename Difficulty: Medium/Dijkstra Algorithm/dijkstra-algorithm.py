import heapq

class Solution:
    def dijkstra(self, V, edges, S):
        
        # Step 1: Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))  # remove if directed

        # Step 2: Dijkstra
        dist = [float('inf')] * V
        dist[S] = 0

        heap = [(0, S)]

        while heap:
            d, u = heapq.heappop(heap)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(heap, (dist[v], v))

        return dist