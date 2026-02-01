A = list(map(int, input().split()))
count = 0

for i in range(0, len(A) - 1):
    if (A[i] != A[i + 1]):
        count += 1

print(count + 1)
