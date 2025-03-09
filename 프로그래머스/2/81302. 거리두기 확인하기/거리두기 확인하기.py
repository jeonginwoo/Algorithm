def solution(places):
    def distance(dot1, dot2):
        return abs(dot1[0]-dot2[0])+abs(dot1[1]-dot2[1])
    
    def checkDist(place):
        person = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    person.append((i, j))
        num = len(person)
        for i in range(num-1):
            for j in range(i+1, num):
                dist = distance(person[i], person[j])
                if dist == 1:
                    return 0
                if dist == 2:
                    a = abs(person[i][0]-person[j][0])
                    if a == 1:
                        x1, y1 = person[i][0], person[j][1]
                        x2, y2 = person[j][0], person[i][1]
                        if place[x1][y1] != 'X' or place[x2][y2] != 'X':
                            return 0
                    else:
                        x, y = (person[i][0]+person[j][0])//2, (person[i][1]+person[j][1])//2
                        if place[x][y] != 'X':
                            return 0
        return 1
        
    answer = []
    for place in places:
        answer.append(checkDist(place))
        
    return answer