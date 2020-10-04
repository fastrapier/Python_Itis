def shift(lst, steps):
    new_list = []
    if steps < 0:
        new_list += lst[steps - 1:]
        new_list += lst[:steps - 1]
        return new_list
    new_list += lst[-steps:]
    new_list += lst[:-steps]

    return newlist


lst = [4, 5, 6, 7, 8, 9, 0]

print(shift(lst, 3))


def has_equal_diff(array):
    boole = True
    for elem in array:
        if elem % array[0] == 0:
            boole = True
        else:
            return False
    return boole


def intersection(a, b, new_type):
    for i in a:
        for j in b:
            if i == j:
                new_type.append(i)
                break
    return new_type
