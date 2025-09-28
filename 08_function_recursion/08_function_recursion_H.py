n = int(input())
m = int(input())

def findGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduceFraction(n, m):
    divisor = findGCD(n, m)

    p = n // divisor
    q = m // divisor

    print(str(p) + ' ' + str(q))

reduceFraction(n, m)