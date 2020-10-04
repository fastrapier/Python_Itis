# init matrix
m = [[1] * 3, [2] * 3, [3] * 3, [4] * 3]
print(*m, sep='\n')
print('==========')

# transpose (way 1) by loops
new_m = []
for col in range(len(m[0])):
    new_row = []
    for row in range(len(m)):
        new_row.append(m[row][col])
    new_m.append(new_row)
print(*new_m, sep='\n')
print('==========')

# transpose (way 2) by zip
new_m = list(zip(*m))
print(*new_m, sep='\n')
print('==========')

# show unpacking
lis = [1, 2, 3, 4]
a = lis[0]
b = lis[1]
c = lis[2]
d = lis[3]
# the same
a, b, *c = lis

# tuple init
a = 2, 3, 4  # tuple
a = (2, 3, 4)  # tuple
a = [2]  # list
a = (2 + 3,)  # tuple
print(a)

# unpack tuple (the same for list)
a = 3
b = 5
c, *a = (b, a)
print(a, b)

# list comprehension
lis = [['i dfdfdfd'] for x in range(10)]
print(lis)

# T1 - самый частый элемент в листе
orig = [1, 1, 3, 3, 3, 4, 4, 2, 2, 3, 2, 2, 1, 1, 3]

# решение 1 вывод с частотой
new = []
uniq = set(orig)
for elem in uniq:
    new.append([elem, orig.count(elem)])

# решение 2 вывод с частотой
new = [[e, orig.count(e)] for e in set(orig)]

# пример обратного порядка
print(sorted(new)[::-1])

# пример работы со строкой
print("abcaaadaa".strip('a'))  # удалить по бокам a
# заменить лишние символы (можно лучше сделать)
a = '+77(65)45-3456'
a = a.replace('+', '').replace('(', '').replace(')', '').replace('-', '')
print(a)

# прост прикол, как убрать дубликаты из листа в листе
# name age height
why = [['Like', 18],
       ['Mike', 18],
       ['Nike', 13, 174],
       ['Like', 18],
       ['Lolik', 28, 181],
       ['Bolik', 10],
       ['Alkogolik', 12, 182]]

# норм решение
new_db = []
for e in why:
    if e not in new_db:
        new_db.append(e)

# как делать НЕ НУЖНО
print(list(map(list, set(map(tuple, why)))))
