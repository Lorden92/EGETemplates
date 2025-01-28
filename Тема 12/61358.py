def f(a):
    for z in range(2, a):
        if a%z==0:
            return False
    return True


c=1000
for x in range(100):
    for y in range(100):
        s = '0' + '1'*x + '2'*y
        if len(s)>40:
            while '01' in s or '02' in s:
                s=s.replace('02', '1110',1)
                s=s.replace('01', '220', 1)
            if f(s.count('1')+s.count('2')*2):
                c = min(c,x+2*y)
print(c)

