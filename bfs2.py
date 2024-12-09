from collections import deque


graph = {"CAB": ("CAT", "CAR"), "CAR": ("BAR", "CAT"), "CAT": ("MAT", "BAT"), "BAR": ("BAT",), "MAT": ("BAT",)}
search_queue = deque()
search_queue += graph["CAB"]
destination = "BAT"
path = 0
temp = 0
levels = [len(graph["CAB"]), 0]
while search_queue:
    point = search_queue.popleft()
    temp += 1
    if temp == levels[path]:
        path += 1
        temp = 0
        levels.append(0)
    if point == destination:
        break
    else:
        search_queue += graph[point]
        levels[path+1] = levels[path+1] + len(graph[point])
print(path)