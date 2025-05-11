def to_ternary(n):
    if n == 0:
        return '0'
    ternary = ''
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
    return ternary


for s in range(1000):
    b = to_ternary(s)
    if s % 3 == 0:
        b += to_ternary(s)[-2:]
    if s % 3 != 0:
        g = b.count('1') + b.count('2') * 2
        b += to_ternary(g)
    r = int(b, 3)
    if r > 220 and r % 2 == 0:
        print(r)
        break
# 222
