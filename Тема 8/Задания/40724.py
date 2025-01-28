from itertools import permutations

count=0
x = 'СВЕТЛАНА'

words = set()

for line in permutations(x, 8):
    line=''.join(line)
    if line.count('АА')==0:
        words.add(line)
        count+=1
print(count//2)
print(len(words))