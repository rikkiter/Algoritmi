size = 35
current_size = 0
bank = 0
items = sorted([(3000, 30), (2000, 20), (1500, 15)], key=lambda x: x[0]/x[1])
for item in items:
    if item[1] + current_size <= size:
        current_size += item[1]
        bank += item[0]
    if current_size == size:
        break
print(bank)