A = list(map(int, input().split()))

count = 0
for i in range(0, len(A)):
    if A[i] > 0:
        count += 1
print(count)