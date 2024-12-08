import sys
from datetime import *
sys.setrecursionlimit(4000)
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

def fibonacciStolbik(n):
    if n == [0] or n == [1]:
        return ([0], [1])[n[0]]
    else:
        return stolbik(fibonacciStolbik(stolbik(n, [-1])), fibonacciStolbik(stolbik(n, [-2])))

test = 39
test2 = [3, 9]
print(test2, test)
a = datetime.now()
fibonacciStolbik(test2)
b = datetime.now()
print(b-a)
print(fibonacciStolbik(test2))

def fibonacci(n):
    if n == 0 or n == 1:
        return (0, 1)[n]
    else:
        return fibonacci(n-1) + fibonacci(n-2)

a = datetime.now()
fibonacci(test)
b = datetime.now()
print(b-a)
print(fibonacci(test))
