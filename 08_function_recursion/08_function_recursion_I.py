n = int(input())


def MinDivisor01(n):
    for i in range(2, n):
        if n % i == 0: return i

    return n


def MinDivisor02(n):
    if n % 2 == 0: return 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return i

    return n


print(MinDivisor01(n))
print(MinDivisor02(n))
