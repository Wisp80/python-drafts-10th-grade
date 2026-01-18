A = list(map(int, input().split()))

for i in range(0, len(A)):
    if (i != 0) and (A[i] > A[i - 1]):
        print(A[i])