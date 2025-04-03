from heapq import *

def solution(N, road, K):
    min_dist = [float('inf')] * (N+1)
    min_dist[1] = 0

    edges = [[] for _ in range(N+1)]
    for a, b, c in road:
        edges[a].append((b, c))
        edges[b].append((a, c))

    heap = [(0, 1)]

    while heap:
        now_w, now_node = heappop(heap)
        
        if now_w > min_dist[now_node]:
            continue
        
        for next_node, next_w in edges[now_node]:
            new_dist = now_w + next_w
            if new_dist < min_dist[next_node]:
                min_dist[next_node] = new_dist
                heappush(heap, (new_dist, next_node))
    
    return sum(1 for d in min_dist if d <= K)
