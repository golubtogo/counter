rainbow_list = 'каждый охотник желает знать где сидит фазан'.split()
for word in rainbow_list:
    print(word)

rainbow_dict = {'каждый': 'красный',
                'охотник': 'оранжевый',
                'желает': 'жёлтый',
                'знать': 'зелёный',
                'где': 'голубой',
                'сидит': 'синий',
                'фазан': 'фиолетовый'}

# Перебираем ключи
for word in rainbow_dict.keys():
    print(word)

# Перебираем значения
for color in rainbow_dict.values():
    print(color)

# Перебираем пары ключ-значение
for word, color in rainbow_dict.items():
    print(word, color)

string = 'Вы - самый крутой студент в SkillFactory'
for letter in string:
    print(letter, end = '')


proverb = 'Программисты - это устройства, преобразующие кофеин в код.'
new_proverb = ''
for i in range(0, len(proverb), 2):
    new_proverb += proverb[i+1] + proverb[i]
print(new_proverb)


basic_word = "программирование"
inverted_word = ""
for i in range(0, len(proverb)):
    inverted_word = basic_word[::-1]
    if basic_word == inverted_word:
        print('Word ' + "'" + inverted_word + "' " + 'is polindrome')
    else:
        print('Word ' + "'" + inverted_word + "' " + 'is not polindrome')
