from itertools import product

x = '012345678'

count = 0

for line in product(x, repeat=6):
    line = ''.join(line)
    if line[0]!='1'and line[0]!='3' and line[0]!='0' and line[0]!='5' and line[0]!='7' and line[5]!='2' and line[5]!='3' and line.count('1')>=2:
        count+=1
print(count)
