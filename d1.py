
def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        left = [int(l.split()[0]) for l in lines]
        right = [int(l.split()[1]) for l in lines]
        left.sort()
        right.sort()
        diff = 0
        for l, r in zip(left, right):
            diff += abs(l - r)
        print("part1:", diff)

def p2(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        left = [int(l.split()[0]) for l in lines]
        right = {}
        for l in lines:
            r = int(l.split()[1])
            if r in right:
                right[r] += 1
            else:
                right[r] = 1
        diff = 0
        for l in left:
            if l in right:
                diff += l * right[l]
        print("part2:", diff)

p1("inputs/d1.txt")
p2("inputs/d1.txt")
