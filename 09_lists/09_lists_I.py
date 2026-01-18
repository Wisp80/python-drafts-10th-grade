A = list(map(int, input().split()))
number = float('inf')
found = False

for b in A:
    if (b % 2 != 0):
        found = True
        if (b < number):
            number = b

if found:
    print(number)
else:
    print(0)