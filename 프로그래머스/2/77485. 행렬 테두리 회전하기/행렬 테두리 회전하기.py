def solution(rows, columns, queries):
    def rotation(query):
        x1, y1, x2, y2 = [x-1 for x in query]
        min_num = float("inf")
        temp = table[x1][y1]
        for j in range(x1, x2):
            min_num = min(min_num, table[j][y1])
            table[j][y1] = table[j+1][y1]
        for i in range(y1, y2):
            min_num = min(min_num, table[x2][i])
            table[x2][i] = table[x2][i+1]
        for j in range(x2, x1, -1):
            min_num = min(min_num, table[j][y2])
            table[j][y2] = table[j-1][y2]
        for i in range(y2, y1, -1):
            min_num = min(min_num, table[x1][i])
            table[x1][i] = table[x1][i-1]
        table[x1][y1+1] = temp
        return min_num
    
    answer = []
    table = [list(range(i, i+columns)) for i in range(1, rows*columns, columns)]
    for query in queries:
        answer.append(rotation(query))
    return answer