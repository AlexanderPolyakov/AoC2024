import re

def mulparse(inp):
    state = -1
    lhs = ''
    rhs = ''
    s = 0
    enabled = True
    s2 = -1
    for symb in inp:
        if enabled:
            if s2 == -1:
                if symb == 'd':
                    s2 = 1
            elif s2 == 1:
                if symb == 'o':
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 2:
                if symb == 'n':
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 3:
                if symb == "'":
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 4:
                if symb == "t":
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 5:
                if symb == "(":
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 6:
                if symb == ")":
                    s2 = -1
                    print("disabled")
                    enabled = False
                    lhs = ''
                    rhs = ''
                    state = -1
                else:
                    s2 = -1

            if state == -1:
                if symb == 'm':
                    state += 1
            elif state == 0:
                if symb == 'u':
                    state += 1
                else:
                    state = -1
            elif state == 1:
                if symb == 'l':
                    state += 1
                else:
                    state = -1
            elif state == 2:
                if symb == '(':
                    state += 1
                else:
                    state = -1
            elif state == 3:
                if ord(symb) >= ord('0') and ord(symb) <= ord('9'):
                    lhs = lhs + symb
                elif symb == ',':
                    state += 1
                else:
                    state = -1
                    lhs = ''
                    rhs = ''
            elif state == 4:
                if ord(symb) >= ord('0') and ord(symb) <= ord('9'):
                    rhs = rhs + symb
                elif symb == ')':
                    state = -1
                    s += int(lhs) * int(rhs)
                    lhs = ''
                    rhs = ''
                else:
                    state = -1
                    lhs = ''
                    rhs = ''
        else:
            if s2 == -1:
                if symb == 'd':
                    s2 = 1
            elif s2 == 1:
                if symb == 'o':
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 2:
                if symb == "(":
                    s2 += 1
                else:
                    s2 = -1
            elif s2 == 3:
                s2 = -1
                if symb == ")":
                    print("enabled")
                    state = -1
                    enabled = True
    return s



def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        s = 0
        for line in lines:
            s += mulparse(line)
        print(s)


p1("inputs/d3.txt")


