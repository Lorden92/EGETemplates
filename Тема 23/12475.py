from functools import lru_cache


@lru_cache(None)
def f(a, step):
    if step == 68:
        numbers.add(a)
        return
    f(a+3,step+1)
    f(a-2, step +1)

numbers = set()

f(1,0)
print(len(numbers))

