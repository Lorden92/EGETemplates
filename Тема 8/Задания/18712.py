import itertools

list_values = itertools.product('ПРАВО', repeat=5)

count = 0
for str in list_values:
    line = ''.join(str)
    if line.count('П')==1:
        count+=1
print(count)