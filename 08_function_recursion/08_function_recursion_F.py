def IsPointInCircle():
    x = float(input())
    y = float(input())

    return (((x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= 2*x + 2 and y >= -1*x) or
            ((x + 1) ** 2 + (y - 1) ** 2 >= 4 and y <= 2*x + 2 and y <= -1*x))

def checkResults():
    if IsPointInCircle():
        print("YES")
    else:
        print("NO")

checkResults()