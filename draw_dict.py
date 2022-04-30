draw_dict = {
    'Польша': 'A',
    'Португалия': 'B',
    'Франция': 'C',
    'Дания': 'C',
    'Египет': 'A'
}

new_dict = {}
for country, group in draw_dict.items():
    if group == 'A':
        new_dict[country] = draw_dict[country]
print(new_dict)


