from collections import deque


n, m = map(int, input().split())
doors = [list(map(lambda x, y: int(x) + y, input().split(), (-1, -1, 0))) for _ in range(m)]
graph = dict([(i, (None,)) for i in range(n)])
for x, y, z in doors:
    if graph[x][0] is None:
        graph[x] = [y]
    elif y not in graph[x]:
        graph[x] = graph[x] + [y]


def bfs(graph):
    search_queue = deque()
    search_queue += graph[0]
    destination = n - 1
    searched = [0]
    while search_queue:
        point = search_queue.popleft()
        if point == destination:
            return True
        else:
            try:
                search_queue += list(set(graph[point]) - set(searched))
            except KeyError:
                continue
            searched.append(point)
    return False


def bellman_ford(n):
    m_infinity = -float("inf")
    dist = [m_infinity] * n
    dist[0] = 0
    if not bfs(graph):
        print(":(")
        return
    for i in range(n-1):
        for u, v, w in doors:
            if dist[u] > m_infinity and dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
    for u, v, w in doors:
        if dist[u] != m_infinity and dist[u] + w > dist[v]:
            print(":)")
            return
    print(dist[-1])


bellman_ford(n)


"""
Условия для графа А
6 9
1 2 5
1 3 2
2 4 4
2 5 2
3 5 7
3 2 8
4 6 3
4 5 6
5 6 1
"""

"""
Условия для графа Б
5 5
1 2 10
2 3 20
3 4 1
3 5 30
4 2 1
"""

"""
Условия для графа С
5 7
1 2 2
1 4 2
2 5 2
2 3 2
3 5 2
3 4 -1
4 2 2
"""

"""
Условия для графа А с противоположным знаком
6 9
1 2 -5
1 3 -2
2 4 -4
2 5 -2
3 5 -7
3 2 -8
4 6 -3
4 5 -6
5 6 -1
"""

"""
Условия для графа Б с противоположным знаком
5 5
1 2 -10
2 3 -20
3 4 -1
3 5 -30
4 2 -1
"""

"""
Условия для графа С с противоположным знаком
5 7
1 2 -2
1 4 -2
2 5 -2
2 3 -2
3 5 -2
3 4 1
4 2 -2
"""


class MangoSeller():
    def __init__(self):
        self.mango_sellers_list = ["semen bakin", "slava kpps", "daniil guskov"]

    def person_is_seller(self, name):
        return name in self.mango_sellers_list

    def add_seller(self, name):
        if name not in self.mango_sellers_list:
            self.mango_sellers_list.append(name)