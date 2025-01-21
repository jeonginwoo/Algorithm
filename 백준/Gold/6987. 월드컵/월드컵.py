import sys
input = sys.stdin.readline

def play_game():
    games = [(i, j) for i in range(5) for j in range(i+1, 6)]

    def backtrack(idx):
        if idx == 15:
            return all(sum(teamResult)==0 for teamResult in gameResult)
        
        team1, team2 = games[idx]
        
        if gameResult[team1][0] > 0 and gameResult[team2][2]:
            gameResult[team1][0] -= 1
            gameResult[team2][2] -= 1
            if backtrack(idx+1):
                return True
            gameResult[team1][0] += 1
            gameResult[team2][2] += 1
        
        if gameResult[team1][1] > 0 and gameResult[team2][1]:
            gameResult[team1][1] -= 1
            gameResult[team2][1] -= 1
            if backtrack(idx+1):
                return True
            gameResult[team1][1] += 1
            gameResult[team2][1] += 1
        
        if gameResult[team1][2] > 0 and gameResult[team2][0]:
            gameResult[team1][2] -= 1
            gameResult[team2][0] -= 1
            if backtrack(idx+1):
                return True
            gameResult[team1][2] += 1
            gameResult[team2][0] += 1
        
        return False

    return backtrack(0)

result = []
for _ in range(4):
    temp = list(map(int, input().split()))
    gameResult = [temp[i:i+3] for i in range(0, len(temp), 3)]
    result.append(1 if play_game() else 0)

print(*result)