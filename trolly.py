import statistics

import statistics

num = [int(x) for x in input("Введите высоту стены через пробел: ").split()]

med = round(statistics.median(num))

count = 0

updated_num = num.copy()

for y in range(len(num)):
    x = num[y]
    while x != med:
        if x < med:
            x = x + 1
        elif x > med:
            x = x - 1

        count += 1
        updated_num[y] = x

        if y == len(num) - 1:
            print(updated_num)
        else:
            print(updated_num, end='=>')

print("\nМинимальное количество ходов:", (count))
