city_list = ['Москва', 'Санкт-Петербург', 'Новосибирск',
             'Екатеринбург', 'Нижний Новгород', 'Казань',
             'Челябинск', 'Омск', 'Самара', 'Ростов-на-Дону']

counter = 0
for city in city_list:
    if ' ' in city or '-' in city:
        counter += 1
print('Число городов со сложными названиями - {}'.format(counter))


tongue_twister = 'Ехал Грека через реку, видит Грека - в реке рак. Сунул Грека руку в реку, рак за руку Греку - цап!'
counter = tongue_twister.count('Грек')
print(counter)

number = 56.257
string = str(number)
sum = 0

for i in string[string.find('.') + 1:]:
    sum += int(i)
print(sum)

