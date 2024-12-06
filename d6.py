import re

def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        grid = []
        pos = None
        for line in lines:
            grid.append([c for c in line[:-1]])
        h = len(grid)
        w = len(grid[0])
        d = [0, -1]
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '^':
                    pos = [x, y]
                    break
        num = 0
        while True:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                break
            if grid[ny][nx] == '#':
                ndx = -d[1]
                ndy = d[0]
                d = [ndx, ndy]
            else:
                pos = [nx, ny]
                if grid[ny][nx] != 'X':
                    grid[ny][nx] = 'X'
                    num += 1
        print(num)

def p2(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        grid = []
        pos = None
        for line in lines:
            grid.append([c for c in line[:-1]])
        h = len(grid)
        w = len(grid[0])
        d = [0, -1]
        for y in range(h):
            for x in range(w):
                if grid[y][x] == '^':
                    pos = [x, y]
                    break
        sx = pos[0]
        sy = pos[1]
        num = 0
        potpos = []
        while True:
            nx = pos[0] + d[0]
            ny = pos[1] + d[1]
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                break
            if grid[ny][nx] == '#':
                ndx = -d[1]
                ndy = d[0]
                d = [ndx, ndy]
            else:
                pos = [nx, ny]
                if grid[ny][nx] != 'X':
                    potpos.append([nx, ny])
                    grid[ny][nx] = 'X'
        for pp in potpos:
            ppx = pp[0]
            ppy = pp[1]
            d = (0, -1)
            pos = [sx, sy]
            crumbs = [[set() for x in range(w)] for y in range(h)]
            while True:
                nx = pos[0] + d[0]
                ny = pos[1] + d[1]
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    break
                if grid[ny][nx] == '#' or (nx == ppx and ny == ppy):
                    ndx = -d[1]
                    ndy = d[0]
                    d = (ndx, ndy)
                else:
                    pos = [nx, ny]
                    beenhere = d in crumbs[ny][nx]
                    if beenhere:
                        num += 1
                        break
                    crumbs[ny][nx].add(d)

        print(num)

p1("inputs/d6.txt")
p2("inputs/d6.txt")

