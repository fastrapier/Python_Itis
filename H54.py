import math


def func1(a, b):
    return tuple((a + b, a * b))


def func2(x, y):
    return math.sqrt(x + math.sqrt(y))


def func3():
    num_list = []
    for i in range(1000, 4251):
        if i % 5 == 0 and i % 3 != 0:
            num_list.append(i)
    print(num_list)


def func4(a):
    if a in range(3, 7):
        a -= 13
    elif a in range(8, 42):
        a -= 50
    elif 0 > a > 2000:
        a *= 4
    else:
        a = 0
    return a


def func5(c):
    return int(9 / 5) * c + 32


def func6(money, percent):
    return money * (percent / 100) * 5


def func7(weeks, months, years):
    days = weeks * 7 + months * 30 + years * 360
    return days


def func8(a):
    nums = []
    simple = 2
    while a > 1:
        if a % simple == 0:
            a /= simple
            nums.append(simple)
        else:
            simple += 1
    return nums


def func9(num):
    divisors = []
    for elem in range(1, num + 1):
        if num % elem == 0:
            divisors.append(elem)
    return divisors


def func10(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))


def func11(num):
    nums = []
    elem = 0
    sequence = 0
    while elem < num:
        elem = sequence ** 2
        if elem < num:
            nums.append(elem)
            sequence += 1
        else:
            break
    return nums


def func12(some_list, coords):
    a = coords[0]
    b = coords[1]
    sum_num = 0
    for i in range(a, b + 1):
        sum_num += some_list[i]
    return sum_num


def func13(a, b):
    some_list = []
    for i in range(a):
        some_list.append(b)
    return some_list


def func14(some_list, num):
    for elem in some_list:
        if elem == num:
            some_list.remove(num)
    return some_list


something = int


def func15(some_num):