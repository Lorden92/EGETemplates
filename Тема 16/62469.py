f = [0]* 3**40
for i in range(3**40):
    if i>15:
        f[i]=i
    if i>=15:
        f[i%15]*f[i//15]
c=0
if f[i]==7560:
    c+=1
print(c)
