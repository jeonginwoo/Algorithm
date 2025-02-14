def solution(m, n, startX, startY, balls):
    def dot_dist(dot1, dot2):
        return (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2
    
    answer = []
    for x, y in balls:            
        cushions = [
            (float('inf'), float('inf')) if y==startY and x<startX else (-x, y),
            (float('inf'), float('inf')) if y==startY and x>startX else (m*2-x, y),
            (float('inf'), float('inf')) if x==startX and y<startY else (x, -y),
            (float('inf'), float('inf')) if x==startX and y>startY else (x, n*2-y)
        ]
        min_dist = float('inf')
        for cushions in cushions:
            min_dist = min(min_dist, dot_dist(cushions, (startX, startY)))
        answer.append(min_dist)
    return answer