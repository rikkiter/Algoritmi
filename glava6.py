from time import sleep
from collections import deque
from random import *


'''Поле лабиринта задаётся нулями и единицами, где ноль выступает в роли стены, а единица - пути'''

test2_labyrinth = [
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
]

test1_labyrinth = [
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 0],
]


class Labyrinth:

    def __init__(self, labyrinth):
        self.width = 8
        self.height = 8
        self.labyrinth = [[randint(0, 1) for _ in range(self.width)] for _ in range(self.height)]
        #self.labyrinth = labyrinth

    def show_labyrinth(self):
        coors = list(str(i) for i in range(self.width))
        print(f'* {" ".join(coors)}')
        print('—'*2*(self.width+1))
        for line, coor in zip(self.labyrinth, coors):
            print(f'{coor}|', end='')
            print(*line)
            sleep(0.3)

    def check_start_n_end(self, start, end):
        if self.labyrinth[start[0]][start[1]] * self.labyrinth[end[0]][end[1]] == 0:
            return -2
        return True

    """В функции create_connections проходимся по всем вершинам графа и если он равна 0, то проверяем соседние на равенство единице.
    Если соседняя равна единице, то добавляем координату в список соседов в словаре, где ключи это координаты вершины"""
    def create_connections(self):
        c = ((-1, 0), (1, 0), (0, 1), (0, -1))
        res = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.labyrinth[i][j] == 1:
                    for neighbor in c:
                        x = i + neighbor[0]
                        y = j + neighbor[1]
                        if 0 <= x <= self.width - 1 and 0 <= y <= self.width - 1 and self.labyrinth[x][y] == 1:
                            res[(i, j)] = res.get((i, j), []) + [(x, y)]
        return res

    def search(self, start, destination):
        graph = self.create_connections()
        search_queue = deque()
        try:
            search_queue += graph[start]
        except KeyError:
            return -1
        searched = [start]
        path = 1
        temp = 0
        levels = [len(graph[start]), 0]
        while search_queue:
            point = search_queue.popleft()
            temp += 1
            levels[path] = levels[path] + len(set(graph[point]) - set(searched))
            if point == destination:
                return path
            else:
                search_queue += list(set(graph[point]) - set(searched))
                searched.append(point)
            if temp == levels[path-1]:
                path += 1
                temp = 0
                levels.append(0)
        return -1


class UI:

    @staticmethod
    def generate():
        for _ in range(3):
            print('----------------')
            print('---GENERATING---')
            sleep(0.4)

    @staticmethod
    def get_coordinate():
        start = input("Введите координаты начала YX\n")
        end = input("Введите координаты конца YX\n")
        return (int(start[0]), int(start[1])), (int(end[0]), int(end[1]))


class Main:

    def __init__(self):
        self.lab = Labyrinth(test1_labyrinth)
        self.UI = UI()

    def run(self):
        self.UI.generate()
        self.lab.show_labyrinth()
        print(self.lab.create_connections())
        while True:
            start, end = self.UI.get_coordinate()
            if self.lab.check_start_n_end(start, end) == -2:
                print(-2)
            else:
                print(self.lab.search(start, end))


Main().run()




