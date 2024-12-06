import re

def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        dirs = [[1, 0], [1, 1], [0, 1], [-1, 0], [-1, -1], [0, -1], [-1, 1], [1, -1]]
        word = "XMAS"
        num = 0
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                for d in dirs:
                    for k in range(len(word)):
                        ii = i + d[0] * k
                        jj = j + d[1] * k
                        if ii < 0 or jj < 0 or ii >= len(lines) or jj >= len(line):
                            break
                        if lines[ii][jj] != word[k]:
                            break
                        if k == len(word) - 1:
                            num += 1
        print(num)

def p2(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        dirs = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
        word = "MAS"
        num = 0
        center_pos = set()
        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(line)):
                for d in dirs:
                    for k in range(len(word)):
                        ii = i + d[0] * k
                        jj = j + d[1] * k
                        if ii < 0 or jj < 0 or ii >= len(lines) or jj >= len(line):
                            break
                        if lines[ii][jj] != word[k]:
                            break
                        if k == len(word) - 1:
                            center = (ii - d[0], jj - d[1])
                            if center in center_pos:
                                num += 1
                            else:
                                center_pos.add(center)

        print(num)


p1("inputs/d4.txt")
p2("inputs/d4.txt")


