A = list(map(int, input().split()))
number = 1000

for i in range(0, len(A)):
    if (A[i] > 0):
        if (A[i] < number):
            number = A[i]

print(number)