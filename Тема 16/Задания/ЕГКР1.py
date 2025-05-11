f = [0] * 20000
for n in range(20000):
    if n < 5:
        f[n] = n
    else:
        f[n] = f[n - 4] * 2 * n
print((f[13766] - 9 * f[13762]) / f[13758])

# 757543052