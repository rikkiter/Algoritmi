from collections import deque


graph = {"CAB": ("CAT", "CAR"), "CAR": ("BAR", "CAT"), "CAT": ("MAT", "BAT"), "BAR": ("BAT",), "MAT": ("BAT",)}
search_queue = deque()
search_queue += graph["CAB"]
destination = "BAT"
path = 0
temp = 0
levels = [len(graph["CAB"])]
while search_queue:
    point = search_queue.popleft()
    temp += 1
    if temp == levels[path]:
        path += 1
        temp = 0
    if point == destination:
        print(point)
        break
    else:
        search_queue += graph[point]
        levels.append(len(graph[point]))
print(path)