def f():
    a = int(input())

    if a == 0:
        print(0)
        return

    f()
    print(a)

f()