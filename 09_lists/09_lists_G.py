A = list(map(int, input().split()))
number = A[0]
index = 0

for i in range(0, len(A)):
    if (A[i] > number):
        number = A[i]
        index = i


print(str(number) + ' ' + str(index))