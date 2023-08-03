import math
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        Q = list(range(n))
        dist = {v:math.inf for v in range(n)}
        prev = n*[None]   # save path in case needed
        dist[0] = 0
        
        while Q:
            u = min(Q, key=dist.get)
            Q.remove(u)
        
            neib = [(x,y,d) for (x,y,d) in edges if x==u and y in Q]
            for (u,v,d) in neib:            
                alt = dist[u] + d
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
        return list(map(lambda x: -1 if x==math.inf else x, dist.values()))
