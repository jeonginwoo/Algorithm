def solution(players, m, k):
    n = len(players)
    server = [0]*(n+k-1)
    answer = 0
    for i in range(n):
        add_server = max(0, players[i] // m - server[i])
        for j in range(i, i+k):
            server[j] += add_server
        answer += add_server
    
    return answer