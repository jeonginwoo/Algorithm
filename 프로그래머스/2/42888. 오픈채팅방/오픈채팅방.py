def solution(record):
    final_nickname = dict()
    for item in record:
        temp = item.split()
        if temp[0] == "Enter" or temp[0] == "Change":
            final_nickname[temp[1]] = temp[2]
    
    answer = []
    for item in record:
        temp = item.split()
        message = f"{final_nickname[temp[1]]}님이 "
        if temp[0] == "Enter":
            answer.append(message+"들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(message+"나갔습니다.")
        
    return answer