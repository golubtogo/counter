# year = 2000
# while year <= 2019:
#     print(year)
#     year += 1
# else:
#     print("Done")

#
# l4 = [i for i in "hello world"]
# l5 = [i for i in "hello world" if i not in ['a', 'e', 'i', 'o', ' ']]
# print(l4, l5, sep="\n")
# print(list(range(0, 10, 2)))

# for i in range(1, 10):
#     print(f"Таблица умножения на {i}")
#     for j in range(0, 9):
#         print(f"\t{i}х{j+1}={i*(j+1)}")

# old_list = [10000, 20000, 30000]
# new_list = []
# for salary in old_list:
#     new_list.append(salary * 2)
# print(new_list)
#
#
# def fact(n):
#     if n==1:  #терминальный случай
#         return 1
#     return n*fact (n-1) #рекурсивный вызов


# print(fact(5))

my_list = []
for x in range(1, 25, 2):
    my_list.append(x)

print(my_list)

my_list2 = [x for x in range(1, 25, 2)]
print(my_list2)

my_list3 = [x for x in range(10, 100) if x % 3 == 0 and x % 5 == 0]
print(my_list3)

powers = [x ** y for x in range(1, 10) for y in [2, 10]]
print(powers)

numbers = [x for x in range(1, 100) if x % 3 == 0 or x % 5 == 0 or x % 7 == 0]
print(numbers)

numbers = [x for x in range(3, 100) if [x % y for y in range(2, x)].count(0) == 0]
print(numbers)

my_list = [x * y for x in range(11, 20) for y in [0.9, 1, 1.1]]
print(my_list)

my_list = []
for x in range(1, 50):
    if x % 7 == 0:
        my_list.append(x ** 0.5)

my_list = [x ** 0.5 for x in range(1, 50) if x % 7 == 0]
print(my_list)

my_list = []
for x in range(90, 100):
    first_digit = x // 10
    last_digit = x % 10
    my_list.append(first_digit + last_digit)

my_list = [x // 10 + x % 10 for x in range(90, 100)]
print(my_list)

employee_base = {
    'Мария Никитина': '+79033923029',
    'Егор Савичев': '+78125849204',
    'Александр Пахомов': '+79053049385',
    'Алина Егорова': '+79265748370',
    'Руслан Башаров': '+79030598495',
}

print(employee_base['Мария Никитина'])
request = ['Мария Никитина', 'Егор Савичев', 'Алексей Чернышевский']
for name in request:
    if name in employee_base:
        print(employee_base[name])
    else:
        print("Неизвесный сотрудник")

draw_dict = {
    'Польша': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}
country = 'Италия'

if country in draw_dict:
    group = draw_dict[country]
else:
    group = 'unknown'
    


