from collections import defaultdict

def solution(friends, gifts):
    idx = {}
    for i in range(len(friends)):
        idx[friends[i]] = i
    
    give = defaultdict(lambda: [0 for _ in range(len(friends))])
    take = defaultdict(lambda: [0 for _ in range(len(friends))])
    zisu = [0 for _ in range(len(friends))]
    for gift in gifts:
        A, B = gift.split()
        give[idx[A]][idx[B]] += 1
        take[idx[B]][idx[A]] += 1
        zisu[idx[A]] += 1
        zisu[idx[B]] -= 1
    print(dict(give))
    print(dict(take))
    print(zisu)
    
    answer = [0 for _ in range(len(friends))]
    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            if give[i][j] > take[i][j]:
                answer[i] += 1
            elif give[i][j] < take[i][j]:
                answer[j] += 1
            elif zisu[i] > zisu[j]:
                answer[i] += 1
            elif zisu[i] < zisu[j]:
                answer[j] += 1
    return max(answer)