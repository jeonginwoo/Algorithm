def solution(land):
    N = len(land)
    M = len(land[0])
    
    visited = [[0]*M for _ in range(N)]
    volumes = dict()
    num = 1
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0 or land[i][j] == 0:
                continue
            visited[i][j] = num
            stack = [(i, j)]
            volume = 1
            while stack:
                nowX, nowY = stack.pop()
                for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nextX, nextY = nowX+d[0], nowY+d[1]
                    if 0 <= nextX < N and 0 <= nextY < M and land[nextX][nextY] == 1 and visited[nextX][nextY] == 0:
                        visited[nextX][nextY] = num
                        stack.append((nextX, nextY))
                        volume += 1
            volumes[num] = volume
            num += 1
    
    answer = 0
    for j in range(M):
        prev = 0
        nums = set()
        for i in range(N):
            now = visited[i][j]
            if now != 0 and prev == 0:
                nums.add(now)
            prev = now
            
        volume = 0
        for num in nums:
            volume += volumes[num]
        answer = max(answer, volume)
    
    return answer