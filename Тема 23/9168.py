
def f(a, step):
    if step==4:
        numbers.add(a)
        return
    f(a+2,step+1)
    f(a*3,step+1)

numbers = set()
f(1,0)
print(len(numbers))