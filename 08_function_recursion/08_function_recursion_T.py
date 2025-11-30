def move(n, x, y):
    if n == 0:
        return

    if (x == 1 and y == 3) or (x == 3 and y == 1):
        d = 2
        move(n - 1, x, y)
        print(str(n) + ' ' + str(x) + ' ' + str(d))
        move(n - 1, y, x)
        print(str(n) + ' ' + str(d) + ' ' + str(y))
        move(n - 1, x, y)

    else:
        z = 6 - x - y
        move(n - 1, x, z)
        print(str(n) + ' ' + str(x) + ' ' + str(y))
        move(n - 1, z, y)

n = int(input())
move(n, 1, 3)