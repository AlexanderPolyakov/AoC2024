import re

def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        rules = []
        rules_end = False
        num = 0
        for line in lines:
            if not rules_end:
                if line == "\n":
                    rules_end = True
                else:
                    rules.append(line[:-1].split("|"))
            else:
                pages = line[:-1].split(",")
                violated = False
                for pidx in range(len(pages)):
                    page = pages[pidx]
                    for rule in rules:
                        if rule[0] == page:
                            for i in range(pidx):
                                if pages[i] == rule[1]:
                                    violated = True
                                    break
                        if violated:
                            break
                    if violated:
                        break
                if not violated:
                    num += int(pages[int(len(pages)/2)])

        print(num)

def p2(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        rules = []
        rules_end = False
        num = 0
        for line in lines:
            if not rules_end:
                if line == "\n":
                    rules_end = True
                else:
                    rules.append(line[:-1].split("|"))
            else:
                pages = line[:-1].split(",")
                violated = False
                while True:
                    curvil = False
                    for pidx in range(len(pages)):
                        page = pages[pidx]
                        for rule in rules:
                            if rule[0] == page:
                                for i in range(pidx):
                                    if pages[i] == rule[1]:
                                        violated = True
                                        curvil = True
                                        print(pages, "violates", rule)
                                        pp = pages[pidx]
                                        pages[pidx] = pages[i]
                                        pages[i] = pp
                    if not curvil:
                        break
                if violated:
                    print("violated", pages)
                    num += int(pages[int(len(pages)/2)])

        print(num)

p1("inputs/d5.txt")
p2("inputs/d5.txt")

