from itertools import product

odd = "1357"
even = "2468"
count = 0

"""
for x1 in odd:
    for x2 in even:
        for x3 in odd:
            for x4 in even:
                for x5 in odd:
                    for x6 in even:
                        for x7 in odd:
                            for x8 in even:
                                for x9 in odd:
                                    for x10 in even:
                                        for x11 in odd:
                                            line = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x10 + x11
                                            if line.count('1') <= 4 and line.count('2') <= 4 and  line.count('3') <= 4 and line.count('4') <= 4 and line.count('5') <= 4 and line.count('6') <= 4 and line.count('7') <= 4 and line.count('8') <= 4:
                                                count += 1
"""

for line in product(odd, even, odd, even, odd, even, odd, even, odd, even, odd):
    line = "".join(line)
    if line.count('1') <= 4 and line.count('2') <= 4 and  line.count('3') <= 4 and line.count('4') <= 4 and line.count('5') <= 4 and line.count('6') <= 4 and line.count('7') <= 4 and line.count('8') <= 4:
        count += 1
print(count * 2)