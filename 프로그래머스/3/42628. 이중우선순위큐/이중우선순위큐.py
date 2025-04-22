from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    min_heap, max_heap = [], []
    visited = defaultdict(bool)
    
    for i, oper in enumerate(operations):
        cmd, num = oper.split()
        num = int(num)
        if cmd == 'I':
            heappush(min_heap, (num, i))
            heappush(max_heap, (-num, i))
            visited[i] = True
        else:
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[heappop(max_heap)[1]] = False
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[heappop(min_heap)[1]] = False
    
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)
    
    if not max_heap or not min_heap:
        return [0, 0]
    return [-max_heap[0][0], min_heap[0][0]]
