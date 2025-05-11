x = 2097152
c=0
for m in range(1, 2097153):
    if x%m==0:
        c+=1
print(c)

