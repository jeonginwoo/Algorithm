def solution(numbers):
    def isTree(bin):
        if len(bin) == 1 or int(bin) == 0:
            return True
        now = len(bin) // 2
        if bin[now] == '0':
            return False
        return isTree(bin[:now]) and isTree(bin[now+1:])
    
    answer = []
    for num in numbers:
        bin_num = str(bin(num))[2:]
        count = 2
        while count-1 < len(bin_num):
            count *= 2
        bin_num = '0'*(count-1-len(bin_num)) + bin_num
        if isTree(bin_num):
            answer.append(1)
        else:
            answer.append(0)
    return answer