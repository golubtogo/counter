new_numbers = []
for number in '3,14 2,71 6,02 11,22 123,987'.split():
    new_numbers.append(float(number.replace(',', '.')))

print(new_numbers)

string = 'Интернет-открытки - это лучшее средство для мужчины сказать женщине о своих чувствах прямо в глаза.'
secret = string[24:30]
new_string = string.replace(secret.lower(), secret.upper())
print(secret)


string = 'Тяжёлая интернет-зависимость - это когда ты выходишь из интернета, а он из тебя нет.'
for i in range(0, len(string)):
    if string[i] in ['.', ',', ':', '-', '!', '?']:
        string = string.replace(string[i], '_')
string = string.replace('_', ':)')
print(string)


name = 'Севастиан'
for letter in name:
    if letter in ['е', 'а', 'и']:
        print('"' + letter +' ' + '- глаcная буква"')
    else:
        print('"' + letter +' ' + '- согласная буква"')