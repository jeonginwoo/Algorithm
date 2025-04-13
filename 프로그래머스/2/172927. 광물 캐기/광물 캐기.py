import math

def solution(picks, minerals):
    idx = {"diamond": 0, "iron": 1, "stone": 2}
    damage = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    
    max_mine = min(len(minerals), sum(picks)*5)
    minerals = minerals[:max_mine]
    new_minerals = [[0, 0, 0] for _ in range(math.ceil(max_mine / 5))]
    for i in range(max_mine):
        new_minerals[i//5][idx[minerals[i]]] += 1
    
    new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))
    answer = 0
    now = 0
    for i in range(3):
        for _ in range(picks[i]):
            if now < len(new_minerals):
                answer += sum([new_minerals[now][j]*damage[i][j] for j in range(3)])
                now += 1
    
    return answer