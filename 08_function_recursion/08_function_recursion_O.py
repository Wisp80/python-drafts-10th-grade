def func(a, res = 0):
    if res == 0:
        res += a

    if a == 0:
        print(res)
    else:
        new = int(input())
        return func(new, res + new)

a = int(input())
func(a)