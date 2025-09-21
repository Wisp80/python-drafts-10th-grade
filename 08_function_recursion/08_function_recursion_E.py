def IsPointInCircle():
    x = float(input())
    y = float(input())
    xc = float(input())
    yc = float(input())
    r = float(input())

    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2

def checkResults():
    if IsPointInCircle():
        print("YES")
    else:
        print("NO")

checkResults()