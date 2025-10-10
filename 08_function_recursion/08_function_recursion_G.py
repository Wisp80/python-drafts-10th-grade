a = float(input())
n = int(input())


def power01(a, n):
    if n == 0: return 1
    if n == 1: return a
    if n < 0: return 1 / power01(a, -n)
    res = float(1)
    for i in range(0, n): res = a * res
    return res


def power02(a, n):
    if n == 0: return 1
    if n == 1: return a
    if n < 0: return 1 / power02(a, -n)

    # 2 ^ 7
    # 2 ^ 8

    # 1 => 2 => 8 => 128
    # 1 => 1 => 1 => 1 => 256
    res = float(1)
    # 2 => 4 => 16 => 256
    # 2 => 4 => 16 => 256 => 65536
    current_a = a
    # 7 => 3 => 1 => 0
    # 8 => 4 => 2 => 1 => 0
    current_n = n

    # 7 - True => 3 - True => 1 - True => 0 - False
    # 8 - True => 4 - True => 2 - True => 1 - True => 0 - False
    while current_n > 0:
        # Если текущая степень нечетная
        # 7 - True => 3 - True => 1 - True
        # 8 - False => 4 - False => 2 - False => 1 - True
        if current_n % 2 == 1:
            # 1 * 2 = 2 => 2 * 4 = 8 => 8 * 16 => 128
            # 1 => 1 => 1 => 1 * 256 = 256
            res = res * current_a

        # Возводим основание в квадрат
        # 2 * 2 = 4 => 4 * 4 = 16 => 16 * 16 = 256
        # 2 * 2 = 4 => 4 * 4 = 16 => 16 * 16 = 256 => 256 * 256 = 65536
        current_a = current_a * current_a
        # Делим степень пополам
        # 7 / 2 = 3.5 (3) => 3 / 2 = 1.5 (1) => 1 / 2 = 0.5 (0)
        # 8 / 2 = 4 => 4 / 2 = 2 => 2 / 1 = 1 => 1 / 2 = 0.5 (0)
        current_n = int(current_n / 2)

    return res


def power03(a, n):
    if n == 0: return 1
    if n == 1: return a
    if n < 0: return 1 / power03(a, -n)

    if n % 2 == 0:
        half = power03(a, n // 2)
        return half * half
    else:
        return a * power03(a, n - 1)


print(power01(a, n))
print(power02(a, n))
print(power03(a, n))
