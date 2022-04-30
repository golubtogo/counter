currency = {
    'AMD': {
        'Name': 'Армянских драмов',
        'Nominal': 100,
        'Value': 13.121
    },

    'AUD': {
        'Name': 'Австралийский доллар',
        'Nominal': 1,
        'Value': 45.5309
    },

    'INR': {
        'Name': 'Индийских рупий',
        'Nominal': 100,
        'Value': 92.9658
    },

    'MDL': {
        'Name': 'Молдавских леев',
        'Nominal': 10,
        'Value': 36.9305
    },
}

# 1 рубль = 0,13131 AMD
# 45.5309
# 0,929658
# 3,69305

values_list = {}

for curr in currency:
    record = currency[curr]
    result = record["Value"]/record["Nominal"]
    values_list.setdefault(curr, result)

print(min(values_list))

