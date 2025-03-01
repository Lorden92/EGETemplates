import sys
sys.setrecursionlimit(900000000)
c = 1
def f(n):
    global c
    c += 1
    print(c)
    if n < 0.00005:
        return n
    else:
        return 0.00002 * n * f(n - 0.00004)

print(f(0.13766))
# print((f(0.13766) - 0.00009 * f(0.13762)) / f(0.13758))

# 757543052