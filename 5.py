from array import *
from random import *
from datetime import *
from time import *

num = 10**11
# spisok1000000000 = [2]*num
# print("Created...")
# print(num)
# array1000000000 = array('i', spisok1000000000)
ar = array('i', [1])
for i in range(num):
    ar.append(1)
print("Created...")
# dict1000000000 = {}
# for i in range(num):
#     dict1000000000[i] = 1
# print("Created...")
# print(num)

# a = time()
# spisok1000000000.append(1)
# b = time()
# print(f'список: {b-a}')


a = time()
ar.append(1)
b = time()
print(f'массив: {b-a}')













# a = time()
# s1 = spisok1000000000[(num-1)]
# b = time()
# print(f'список: {b-a}')
#
# a = time()
# a1 = array1000000000[(num-1)]
# b = time()
# print(f'массив: {b-a}')

# a = time()
# d1 = dict1000000000[num-1]
# b = time()
# print(f'словарь: {b-a}')

#################################


# a = datetime.now()
# s1 = spisok1000000000[num-1]
# b = datetime.now()
# print(b-a)
#
# a = datetime.now()
# a1 = array1000000000[num-1]
# b = datetime.now()
# print(b-a)

#
# a = datetime.now()
# d1 = dict1000000000[num-1]
# b = datetime.now()
# print(b-a)
# print(s1, a1, d1)