count_money = {
    '2019-04-01': 2504,
    '2019-04-02': 4994,
    '2019-04-03': 6343
}
money_sum = 0
for date, money in count_money.items():
    money_sum += money
print(money_sum)
