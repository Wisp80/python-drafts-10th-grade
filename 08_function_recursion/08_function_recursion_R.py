def gcd(a, b):
    if b == 0:
        return a
    if a % b == 0 or b % a == 0:
        if a >= b:
            return b
        else:
            return a
    else:
        return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))