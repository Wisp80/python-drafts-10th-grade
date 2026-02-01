A = list(map(int, input().split()))
x = int(input())

pos = 0
while (pos < len(A) and A[pos] >= x):
    pos += 1
print(pos + 1)