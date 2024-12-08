def binary_search(list, item):
    low = 0
    high = len(list) - 1
    counter = 0
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            counter += 1
            high = mid - 1
        else:
            counter += 1
            low = mid + 1

birthdays = [(2004, 8, 22), (2004, 11, 21), (2004, 12, 19), (2005, 1, 18), (2005, 3, 11), (2005, 8, 18), (2005, 8, 19)]

print(f'Индекс искомого элемента {binary_search(birthdays, (2004, 12, 19))}')

print(f'1. {[2004, 11, 21] < [2005, 1, 18]}')
print(f"2. {[2005, 1, 18] > [2005, 1, 19]}")
print(f"3. {[2005, 1, 18, 6] > [2005, 1, 19]}")
print(f"4. {[2005, 1, 19] < [2005, 1, 19, 1]}")
print(f"5. {('winter', 'spring', 'summer') == ('winter', 'spring', 'summer')}")
print(f"6. {('winter', 'spring', 'summer') > ('winter', 'spring', 'summer', 'fall')}")
print(f"7. {('winter', 'spring', 'summer') < ('winter', 'spring', 'summer', 'fall')}")
#
# print(f'1. {[2004, 11, 21] < [2004, 11, "fall"]}')
