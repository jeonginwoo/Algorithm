X = input()

a = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

answer = 0
if X[0] == '0':
    mul = 1
    if X[1] == 'x':
        for i in range(len(X)-1, 1, -1):
            answer += a[X[i]] * mul
            mul *= 16
    else:
        for i in range(len(X)-1, 0, -1):
            answer += a[X[i]] * mul
            mul *= 8
else:
    answer = int(X)

print(answer)