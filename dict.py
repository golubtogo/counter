simple_dict = {'a': 1}
simple_dict.setdefault('b', 0)
print(simple_dict)

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
    draw_dict.setdefault(country, 'unknown')


employee_base = {
    'Мария Никитина': 'менеджер',
    'Егор Савичев': 'разработчик',
    'Александр Пахомов': 'дизайнер',
    'Алина Егорова': 'разработчик',
    'Руслан Башаров': 'верстальщик'
}

# for employee in employee_base:
#     print(employee)

# for employee in employee_base:
#     print(employee, employee_base[employee])

# for employee in employee_base:
#     if employee_base[employee] == 'разработчик':
#         print(employee)


# draw_dict = {
#     'Россия': 'A',
#     'Португалия': 'B',
#     'Франция': 'C',
#     'Дания': 'C',
#     'Египет': 'A'
# }
# new_dict = {}
# for country in draw_dict:
#     if draw_dict[country] == 'A':
#         new_dict[country] = draw_dict[country]
#
# print(new_dict)
#
# counter = 0
# for position in employee_base.values():
#     if position == 'разработчик':
#         counter = counter + 1
# print(counter)


for employee, positions in employee_base.items():
    print(employee, positions)


for employee, position in employee_base.items():
    if position == 'разработчик':
        print(employee)






