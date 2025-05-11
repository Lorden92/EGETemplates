values = [0] * 300000000

for n in range(len(values)):
    if n == 0:
        values[n] = 0
    elif n > 0 and n % 4 < 2:
        values[n] = values[n // 4] + n % 4
    elif n % 4 >= 2:
        values[n] = values[n // 4] + n % 4 - 1
    if values[n] == 16 and values[n - 1] == 27:
        print(n)
        break
