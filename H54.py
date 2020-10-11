import math
import ipaddress
import random
import numpy as np


def func1(a, b):
    return a + b, a * b


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
    return weeks * 7 + months * 30 + years * 360


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
    sum_num = 0
    for i in range(coords[0], coords[1]):
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


def func15(some_num):
    min_num = 0
    max_num = 0
    for digit in some_num:
        min_num = min(min_num, digit)
        max_num = max(max_num, digit)
        print(digit)
    return max_num, min_num


def func16(num):
    array = list(map(int, str(num)))
    flag = False
    for elem in range(len(array) - 1):
        if max(array[elem], array[elem + 1]) == array[elem]:
            flag = True
        else:
            flag = False
            break
    return flag


def func17(some_list):
    return some_list == some_list[::-1]


def z18(*args, string):
    return ' '.join([word for word in string.split() if not any(letter in word for letter in args)])


def func19(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True


def func20(string):
    digits = set("0123456789")
    only_digits = ""
    for digit in string:
        if digit in digits:
            only_digits += digit
    return only_digits


def func21(*args):
    even = 0
    odd = 0
    for elem in args:
        if elem % 2 == 0:
            even += elem
        else:
            odd += elem
    return even / 2, odd / 2


def func22(array):
    return [elem for elem in array if elem != 0]


def func23(array, some_int):
    blizayshee = 10000
    for elem in array:
        blizayshee = min(blizayshee, abs(elem - some_int))

    for i in array:
        if abs(i - some_int == blizayshee):
            return i


def func24(predlozheniye):
    vowels = set("аоуеияёэю")
    new_string = ""
    for letter in predlozheniye:
        if letter in vowels:
            new_string += letter + 'c' + letter
        else:
            new_string += letter

    return new_string


# def func25(array):
#     max_sum = 0
#     ans = {}
#     for i in range(1, len(array)):
#         ans.update({[array[i - 1], array[i], array[i + 1]]: [i - 1, i, i + 1]})
#     for elem in ans:
#         print(elem)


def func26(array):
    some_map = {}
    for i in array:
        some_map.update({i: list(array).count(i)})
    some_list = some_map.values()
    for elem in some_list:
        if elem > 1:
            return False
        else:
            return True


def func27(array):
    counter = 0
    arr_max = max(array)
    for elem in array:
        if elem * 0.1 <= arr_max:
            counter += 1
    return counter


def func28(c, a, b):
    new_list = []
    for elem in c:
        if elem in range(a + 1, b):
            new_list.append(-elem)
        else:
            new_list.append(elem)
    return new_list
    # else in return
    # return [-elem for elem in c if elem in range(a + 1, b)]


def func29(arr1, arr2):
    return arr1 == arr2


def func30(arr):
    new_arr = arr
    new_arr.sort(key=lambda x: not x)
    return new_arr


def func31(some_list):
    counter = 0
    new_list = []
    for elem in some_list:
        if counter % 2 == 0:
            new_list.append(elem)
        counter += 1
    return new_list


def func32(array):
    return [i for i in range(1, len(array)) if array[i - 1] < array[i] >= array[i + 1]]


def func33(array):
    local_max = []
    for i in range(1, len(array) - 1):
        if array[i - 1] < array[i] >= array[i + 1]:
            local_max.append(i)
    print(local_max)
    for index in range(1, len(local_max)):
        return [local_max[index] - local_max[index - 1] - 1]


def func34(digit):
    months = {1: "December", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
              9: "September", 10: "November", 11: "October", 12: "December"}
    return months.get(digit)


def func35(digit):
    season = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
              9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
    return season.get(digit)


def func36(list1, list2):
    return dict(zip(list1, list2))


def func37(some_map):
    pass


def func38(some_map):
    return {v: k for k, v in some_map.items()}


def func39(some_map):
    pass


def func40(n):
    return {i: i ** 2 for i in range(1, n + 1)}


def func41(a, b):
    list = []
    for row in range(a):
        new_list = []
        for elems in range(b):
            new_list.append(random.randint(1, 100))
        list.append(new_list)
    return list


def func42(matrix):
    max_list = []
    min_list = []
    for row in matrix:
        max_list.append(max(row))
        min_list.append(min(row))
    return [max(max_list), min(min_list)]


def func43(matrix_):
    return [max(row) for row in matrix_]


def func44(matrix_new):
    a = np.array(matrix_new)
    a = a.transpose()
    return [max(row) for row in a]


def func45(new_matr):
    max_list = []
    for i, elem in enumerate(new_matr):
        max_list.append(max(elem))
    max_elem = max(max_list)
    for i in range(len(new_matr)):
        for j in range(len(new_matr[i])):
            if new_matr[i][j] == max_elem:
                new_matr[i][j] = 0
    return new_matr
