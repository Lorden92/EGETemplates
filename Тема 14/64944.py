for p in range(36):
    for x in range(1,p):
        for y in range(1,p):
            for z in range(1,p):
                for w in range(1,p):
                    res = z*p**4+x*p**3+y*p**2+x*p**1+7
                    res1 = x*p**4+y*p**3+8*p**2+3*p**1+6
                    fin = w*p**4+z*p**3+x*p**2+6*p**1+4
                    if res+res1 == fin:
                        print(x*p**3+y*p**2+z*p**1+w*p**0)

