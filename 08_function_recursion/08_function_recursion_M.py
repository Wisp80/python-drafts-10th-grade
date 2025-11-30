def phib(n):
    if n == 1 or n == 2:
        return 1

    t = phib(n - 1) + phib(n - 2)
    return t

n = int(input())
print(phib(n))