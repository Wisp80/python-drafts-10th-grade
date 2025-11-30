def move(n, x, y):
    if n == 1:
        print(str(n) + ' ' + str(x) + ' ' + str(y))
    else:
        z = 6 - x - y
        move(n - 1, x, z)
        print(str(n) + ' ' + str(x) + ' ' + str(y))

        move(n - 1, z, y)

n = int(input())
move(n, 1, 3)