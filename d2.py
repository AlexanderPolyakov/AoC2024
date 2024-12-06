
def p1(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        reports = [l.split() for l in lines]
        num = 0
        for r in reports:
            nums = [int(n) for n in r]
            dr = nums[1] - nums[0]
            safe = True
            for p, c in zip(nums[:-1], nums[1:]):
                if (c - p) * dr < 0 or abs(c - p) < 1 or abs(c - p) > 3:
                    safe = False
                    break
            if safe:
                num += 1
        print(num)

def isgood(nums, dr):
    for i in range(1, len(nums)):
        p = nums[i-1]
        c = nums[i]
        if (c - p) * dr < 0 or abs(c - p) < 1 or abs(c - p) > 3:
            return i
    return -1

def p2(fname):
    with open(fname, "rt") as f:
        lines = f.readlines()
        reports = [l.split() for l in lines]
        num = 0
        for r in reports:
            nums = [int(n) for n in r]
            dr = nums[1] - nums[0]
            res = isgood(nums, dr)
            if res < 0:
                num += 1
            else:
                newnums = nums[:res] + nums[res+1:]
                dr = newnums[1] - newnums[0]
                if isgood(newnums, dr) < 0:
                    print(nums)
                    num += 1
                    #break
        print(num)

p1("inputs/d2.txt")
p2("inputs/d2.txt")

