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


emails_dict = {}
emails_list = ['vasya@mail.ru',
          'akakiy@yandex.ru',
          'spyderman@yandex.ru',
          'XFiles@gmail.com',
          'hello@mail.ru',
          'noname@gmail.com',
          'DonaldTrump@mail.ru',
          'a768#af@yandex.ru',
          'Ivan_Ivanovich@yandex.ru',
          'thebestmail@yandex.ru']
for email in emails_list:
    domain = email[email.find('@')+1:]
    emails_dict.setdefault(domain, 0)
    emails_dict[domain] += 1
print(emails_dict)




