bodycount = {
    'Проклятие Черной жемчужины': {
        'человек': 17
    },

    'Сундук мертвеца': {
        'человек': 56,
        'раков-отшельников': 1
    },

    'На краю света': {
        'человек': 88
    },

    'На странных берегах': {
        'человек': 56,
        'русалок': 2,
        'ядовитых жаб': 3,
        'пиратов зомби': 2
    }
}

# 17+56+1+88+56+2+3+2 = 225

count = {}
body_sum = 0
for body in bodycount:
    for people, count in bodycount[body].items():
        body_sum += count
print(body_sum)



