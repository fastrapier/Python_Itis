import math


def merge_list(*args): return args


list_to_merge = [[1, 8, 3], [-5, 0], [4], [2, 3, 3]]


# 1
def merge_list2(something):
    another_list = []
    for row in something:
        for elem in row:
            another_list.append(elem)
    return another_list


print(merge_list2(list_to_merge))
print('---------------------------------------')

# 2
original = (3, 2, 0, -2, -7)
power = (1 / 3, 7, 10, -2, 3)


def pow_pow_pow(originals, powers):
    new_list = []
    for elem in originals:
        for stepen in powers:
            if elem == 0:
                new_list.append(0.0)
            else:
                new_list.append(pow(elem, stepen))
            break
    return new_list


print(pow_pow_pow(original, power))
print('---------------------------------------')

# 3
list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]


def rm_elems(list1):
    list2 = []

    for line in list1:
        list2.append([])
        for elem in line:
            for line_2 in list2:
                if elem in line_2:
                    break
            else:
                list2[-1].append(elem)
    return list2


print(rm_elems(list_of_lists))
print('---------------------------------------')
# 4
unchangeable = ([1, 2], [3, 4], [5, 6])


def expand(unchangeablee, index=None, expanby=None):
    new_list = []
    for i in range(len(unchangeablee)):
        new_list.append(unchangeable[i])
        if i == index:
            for elem in expanby:
                new_list[i].append(elem)
    return tuple(new_list)


print(expand(unchangeable, index=2, expanby=[99, 0]))
print('---------------------------------------')
