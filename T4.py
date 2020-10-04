def new_func(some_list, *args, sum=bool):
    if sum:
        num_sum = 0
        for elem in args:
            num_sum += elem
    return num_sum


print(new_func(1, 2, 3, 4, 5, 6, 7, 8, sum=True))
