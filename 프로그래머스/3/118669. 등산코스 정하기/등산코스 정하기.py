import heapq

def solution(n, paths, gates, summits):
    # 그래프 생성
    edges = [[] for _ in range(n+1)]
    for i, j, w in paths:
        edges[i].append((j, w))
        edges[j].append((i, w))

    # 출입구와 산봉우리 집합으로 변환
    gates = set(gates)
    summits = set(summits)

    # 다익스트라: intensity 최소화
    def dijkstra():
        pq = []
        intensity = [float("inf")] * (n + 1)

        # 모든 출입구에서 시작
        for gate in gates:
            heapq.heappush(pq, (0, gate))  # (현재 intensity, 노드)
            intensity[gate] = 0
        
        while pq:
            curr_intensity, node = heapq.heappop(pq)
            
            # 산봉우리 도착하면 탐색 종료
            if node in summits or curr_intensity > intensity[node]:
                continue
            
            # 인접 노드 탐색
            for next_node, weight in edges[node]:
                new_intensity = max(curr_intensity, weight)  # 현재까지 경로 중 최댓값 유지
                if new_intensity < intensity[next_node]:  # 더 작은 intensity라면 업데이트
                    intensity[next_node] = new_intensity
                    heapq.heappush(pq, (new_intensity, next_node))

        return intensity

    # 다익스트라 실행
    intensity = dijkstra()

    # 가장 작은 intensity를 가진 산봉우리 선택
    answer = []
    min_intensity = float("inf")
    for summit in sorted(summits):  # 산봉우리 오름차순
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            answer = [summit, min_intensity]

    return answer
