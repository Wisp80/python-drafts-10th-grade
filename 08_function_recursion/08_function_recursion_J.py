x = int(input())


def IsPrime01(x):
    if x == 1 or x == 2:
        print('YES')
        return True

    for i in range(2, x):
        if x % i == 0:
            print('NO')
            return False

    print('YES')
    return True


def IsPrime02(x):
    if x == 1 or x == 2:
        print('YES')
        return True

    if x % 2 == 0:
        print('NO')
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            print('NO')
            return False

    print('YES')
    return True


IsPrime01(x)
IsPrime02(x)