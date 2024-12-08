# import traceback
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return (0, 1)[n]
#     else:
#         print(f'Computing F{n} recursively...')
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))


# def sum(list):
#     if list == []:
#         return 0
#     return list[0] + sum(list[1:])
# print(sum([1, 3, 4 ,3 , 454, 54 ,35, 35345, 53453]))
#
# def count(list):
#     if list == []:
#         return 0
#     return 1+1*count(list[1:])
#
# print(count([1, 3, 4 ,3 , 454, 54 ,35, 35345, 53453]))
#
# def max(lst):
#     if len(lst) == 0:
#         return None
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_num = max(lst[1:])
#         return lst[0] if lst[0] > max_num else max_num

# print(max([1, 3, 4 ,3 ,53453, 454, 54 ,35, 35345]))

for i in range(1945, 2040):
    years = {0: "Дракон", 1: "Змея", 2: "Лошадь", 3: "Овца", 4: "Обезьяна", 5: "Петух", 6: "Собака", 7: "Свинья", 8: "Крыса", 9: "Бэк", 10: "Тигр", 11: "Заяц"}
    print(i, '=', years[((12-abs(2000-i)) % 12)], ((12-abs(2000-i)) % 12))