import itertools
list_values = itertools.product('АНДРЕЙ', repeat=4)
count = 0
for str in list_values:
    line = ''.join(str)
    if (line.count('А') + line.count('Е')) >= 1 and line[0]!='Й':
        count+=1
print(count)

