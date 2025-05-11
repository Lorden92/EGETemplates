from itertools import permutations


def f(a):
    for v in range(2, int(a ** 0.5) + 1):
        if a % v == 0:
            return False
    return True


for z in range(20):
    for w in range(20):
            s = '0' +  + '0'
            while '00' not in s:
                s = s.replace('033', '21120', 1)
                s = s.replace('034', '22120', 1)
                s = s.replace('04', '220', 1)
                s = s.replace('030', '100', 1)
            if len(s) == 65 and f(s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4):
                print(w)
