A = list(map(int, input().split()))
B = []

for i in range(len(A) - 1, -1, -1):
    B.append(A[i])

A = B
print(*A)