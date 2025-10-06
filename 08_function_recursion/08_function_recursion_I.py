n = int(input())

def MinDivisor(x):
    for i in range(2, x + 1):
        if x % i == 0:
            print(i)
            return
    print(x)

MinDivisor(n)