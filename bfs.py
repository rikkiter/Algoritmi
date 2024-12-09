from collections import deque


graph = {"S": ("A", "C"), "A": ("B", "F"), "C": ("B", "D"), "D": ("F",), "B": (None,)}
search_queue = deque()
search_queue += graph["S"]
destination = "F"
path = 0
temp = 0
levels = [len(graph["S"]), 0]
while search_queue:
    point = search_queue.popleft()
    temp += 1
    if temp == levels[path]:
        path += 1
        temp = 0
        levels.append(0)
    if point == destination:
        print(point)
        break
    else:
        search_queue += graph[point]
        levels[path+1] = levels[path+1] + len(graph[point])
print(path)