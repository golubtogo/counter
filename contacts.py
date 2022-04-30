contacts = {

    'Борискин Владимир': {
        'tel': '5387',
        'position': 'менеджер'
    },

    'Сомова Наталья': {
        'tel': '5443',
        'position': 'разработчик'
    },
}

print(contacts['Борискин Владимир']['tel'])


csv_dict = [
    {'id': '100412', 'position': 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 'count': 9},
    {'id': '100728', 'position': 'Скейтборд Jdbug RT03', 'count': 32},
    {'id': '100732', 'position': 'Роллерсерф Razor RipStik Bright', 'count': 11},
    {'id': '100803', 'position': 'Ботинки для сноуборда DC Tucknee', 'count': 20},
    {'id': '100898', 'position': 'Шагомер Omron HJA-306', 'count': 2},
    {'id': '100934', 'position': 'Пульсометр Beurer PM62', 'count': 17},
]

csv_dict_boots = []

for record in csv_dict:
    if 'Ботинки' in record['position']:
        print(record)


results = [
    {'cost': 98, 'source': 'vk'},
    {'cost': 153, 'source': 'yandex'},
    {'cost': 110, 'source': 'facebook'},
]

numbers = []
for record in results:
    numbers.append(record['cost'])
print(min(numbers))

defect_stats = [
    {'step number': 1, 'damage': 0.98},
    {'step number': 2, 'damage': 0.99},
    {'step number': 3, 'damage': 0.99},
    {'step number': 4, 'damage': 0.96},
    {'step number': 5, 'damage': 0.97},
    {'step number': 6, 'damage': 0.97},
]

damage = 1
counter = 0

for record in defect_stats:
    if damage > 0.9:
        damage = damage*record['damage']
        counter += +1
print(counter)




