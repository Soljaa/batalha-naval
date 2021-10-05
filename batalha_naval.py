import random
import numpy as np


def gen_boat1(g):
    name = 'Corveta'
    size = 1
    count = 4
    x = 0
    while x < count:
        coord = random.randint(0, 9), random.randint(0, 9)
        if g[coord] == 0:
            g[coord] = 1
            x += 1


def gen_boat2(g):
    name = 'Fragata'
    size = 2
    count = 3
    x = 0
    while x < count:
        coord = random.randint(0, 8), random.randint(0, 8)
        coord2 = (coord[0]+1, coord[1])
        if g[coord] == 0 and g[coord2] == 0:
            g[coord] = 1
            g[coord2] = 1
            x += 1


def gen_boat3(g):
    name = 'Porta-Aviões'
    size = 3
    count = 2
    x = 0
    while x < count:
        coord = random.randint(0, 7), random.randint(0, 7)
        coord2 = (coord[0], coord[1] + 1)
        coord3 = (coord2[0], coord2[1] + 1)
        if g[coord] == 0 and g[coord2] == 0 and g[coord3] == 0:
            g[coord] = 1
            g[coord2] = 1
            g[coord3] = 1
            x += 1


def grade(x, y):
    grid = np.zeros((x, y), dtype=int)
    gen_boat1(grid)
    gen_boat2(grid)
    gen_boat3(grid)
    return grid


grade = grade(10, 10)



