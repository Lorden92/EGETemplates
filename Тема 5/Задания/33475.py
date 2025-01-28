for n in range(2, 100):
    b = bin(n)[2:]
    b += b[-2]
    b += b[1]
    r = int(b, 2)
    if r>180:
        print(n)
        break
