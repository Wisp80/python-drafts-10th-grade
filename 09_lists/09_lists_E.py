A = list(map(int, input().split()))

for i in range(0, len(A) - 1):
    if (A[i] > 0) and (A[i + 1] > 0):
        print(A[i])
        print(A[i + 1])
        break

    if (A[i] < 0) and (A[i + 1] < 0):
        print(A[i])
        print(A[i + 1])
        break