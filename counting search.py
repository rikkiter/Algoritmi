# сортировка подсчетом массива, в котором значения могут быть от 0 до 100
from datetime import *
from random import *


def counting_sort(some_list):
    counting_list = [0] * 10000
    for elem in some_list:
        counting_list[elem] += 1
    result = []
    for num in range(10000):
        if counting_list[num] != 0:
            result.extend([num]*counting_list[num])
    return result


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


for n in range(7, 15):
    print(f'10**{n}')
    list1 =[randint(0, 9999) for _ in range(10**n)]
    a = datetime.now()
    counting_sort(list1)
    b = datetime.now()
    print(f'counting_sort: {b - a}')

    a = datetime.now()
    quicksort(list1)
    b = datetime.now()
    print(f'quicksort: {b-a}')