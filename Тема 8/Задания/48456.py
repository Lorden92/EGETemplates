from itertools import product

x = '012345678'

count = 0

for line in product(x, repeat=6):
    line = ''.join(line)
    if line.count('4')==1 and (line.count('1')+line.count('3')+line.count('5')+line.count('7')==2) and line[0]!='0':
        count+=1
print(count)