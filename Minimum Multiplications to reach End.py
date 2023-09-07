from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        queue = deque([(start, 0)])
        visited = set()
        
        while queue:
            curr, steps = queue.popleft()
            
            if curr == end:
                return steps
            
            for num in arr:
                next_val = (curr * num) % 100000
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append((next_val, steps + 1))
        
        return -1
