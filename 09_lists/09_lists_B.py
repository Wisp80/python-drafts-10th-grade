A = list(map(int, input().split()))

for i in range(0, len(A)):
    if A[i] % 2 == 0:
        print(A[i])