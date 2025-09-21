x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def distance(x1, y1, x2, y2):
    res = ( abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 ) ** 0.5
    return res

print(distance(x1, y1, x2, y2))