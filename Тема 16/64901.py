def f(n):
    if n==0: return 1
    if n%2!=0: return (n%10)*f(n//100)
    if n%2==0: return f(n//100)
c = 0
for a in range(10**7,8*10**7+1):
    if f(a)==35:
        c+=1
print(c)