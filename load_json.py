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


table_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'table':
        table_clients.append(client_id)
print(table_clients)


c = collections.Counter()
for table_clients in table_clients:
    c[table_clients] += 1
print(c)

print(len(c.keys()))
print(c[60459])


table_all_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    table_all_clients.append(client_id)

print(table_all_clients)


c = collections.Counter()
for table_all_clients in table_all_clients:
    c[table_all_clients] += 1


print(c)
print(len(c.keys()))
print(c[60459])


page_clients = []
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'page':
        page_clients.append(client_id)
print(c)
print(c[62602])


report_clients = {}
for item in data_list:
    client_id = item['client_id']
    category = item['category']
    if category == 'report':
        report_clients.setdefault(client_id)
print(len(report_clients))
print(report_clients)


