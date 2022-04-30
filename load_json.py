import json
import collections

with open('data.json', 'rb') as infile:
    data = json.load(infile)

    print(type(data))
    print(data.keys())
    print(data['events_data'])
    data_list = data['events_data']
    print(len(data_list))

categories = []

for item in data_list:
    category = item['category']
    categories.append(category)
print(categories)

c = collections.Counter()
for category in categories:
    c[category] += 1
print(c)
