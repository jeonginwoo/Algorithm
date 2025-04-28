from collections import defaultdict

def solution(genres, plays):
    n = len(genres)
    genre_count = defaultdict(int)
    for i in range(n):
        genre_count[genres[i]] += plays[i]
    infos = sorted([(genres[i], genre_count[genres[i]], plays[i], i) for i in range(n)], key=lambda x: (-x[1], -x[2], x[3]))
    
    now = infos[0][0]
    count = 0
    answer = []
    for genre, _, __, i in infos:
        if now == genre and count == 2:
            continue
        
        if now == genre:
            count += 1
        else:
            now = genre
            count = 1
        answer.append(i)
        
    return answer