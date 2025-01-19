import sys
input = sys.stdin.readline
MAX_NUM = 10000000000

def find_dec_num(size:int, pre_dec_size:int):
    if size >= MAX_NUM:
        return
    now_dec_size = len(decList)
    temp = decList[pre_dec_size:]
    k = temp[0] // size
    for i in range(k+1, 10):
        for j in temp:
            if i > j // size:
                decList.append(i*size*10 + j)
            else:
                break
    find_dec_num(size*10, now_dec_size)
        
decList = [x for x in range(10)]
find_dec_num(1, 0)

N = int(input())
print(decList[N] if len(decList) > N else -1)