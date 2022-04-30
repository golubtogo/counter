csv_file = [
    ['100412', 'Ботинки для горных лыж ATOMIC Hawx Prime 100', 9],
    ['100728', 'Скейтборд Jdbug RT03', 32],
    ['100732', 'Роллерсерф Razor RipStik Bright', 11],
    ['100803', 'Ботинки для сноуборда DC Tucknee', 20],
    ['100898', 'Шагомер Omron HJA-306', 2],
    ['100934', 'Пульсометр Beurer PM62', 17],
]

# print(csv_file[4][2])
#
# pulsometer_id = csv_file[5][0]
# print(pulsometer_id)

# for record in csv_file:
#     if record[1] == 'Шагомер Omron HJA-306':
#         print('Количество шагомеров на складе - {}шт'.format(record[2]))


csv_file_filtered = []

for record in csv_file:
    if record[2] >= 10:
        csv_file_filtered.append(record)
print(csv_file_filtered)






