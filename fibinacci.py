from datetime import *

def stolbik(num1, num2):
    if len(num1) != len(num2):
        result = [0] + max(num1, num2, key=len)
        small = min(num1, num2, key=len)
    else:
        result = [0] + num1
        small = num2
    small_len = len(small)
    for i in range(1, small_len + 1):
        temp = result[-i] + small[-i]
        result[-i] = temp % 10
        result[-i-1] = result[-i-1] + temp // 10
    while True:
        if result[0] != 0 or len(result) == 1:
            break
        else:
            del result[0]
    return result

def fibanacci(n):
    fst, snd = 0, 1
    for i in range(n):
        fst, snd = snd, fst + snd
    return fst

def fibanacciStolbik(n):
    fst, snd = [0], [1]
    for i in range(n):
        fst, snd = snd, stolbik(fst, snd)
    return fst

num = 10**5
print(num)

a = datetime.now()
fibanacci(num)
b = datetime.now()
print(str(b-a))
print(fibanacci(num))


a = datetime.now()
fibanacciStolbik(num)
b = datetime.now()
print(str(b-a))
print(fibanacciStolbik(num))

100000
0:00:00.107023
0:07:10.439200