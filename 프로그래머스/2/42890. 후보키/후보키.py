from itertools import combinations

def solution(relation):
    col = len(relation[0])
    row = len(relation)
    
    combi = []
    for i in range(1, col+1):
        combi += list(combinations(range(col), i))
    
    unique = []
    for select in combi:
        check = set([tuple(item[i] for i in select) for item in relation])
        if len(check) == row:
            unique.append(select)
    print(unique)
    
    answer = set(unique)
    for i in range(len(unique)-1):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    
    return len(answer)