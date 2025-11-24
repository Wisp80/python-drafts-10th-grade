def func(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        t = func(a, n // 2)
        return t * t
    else:
        return a * func(a, n - 1)


a = float(input())
n = int(input())
print(func(a, n))