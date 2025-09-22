def power(a, n):
    if n == 1:
        print(a)
    else:
        res = float(1)
        for i in range(0, n):
            res = a * res

        print(res)

a = float(input())
n = int(input())

power(a, n)