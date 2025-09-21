def IsPointInSquare():
    x = float(input())
    y = float(input())
    return abs(x) <= 1 and abs(y) <= 1

def checkResults():
    if IsPointInSquare():
        print("YES")
    else: 
        print("NO")

checkResults()