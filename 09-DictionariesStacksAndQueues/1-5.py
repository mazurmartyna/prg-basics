countries = [
{"name":"Poland", "population":38000000},
{"name":"France", "population":68170000},
{"name":"Italy", "population":59660000},
{"name":"Japan", "population":124500000},
{"name":"Germany", "population":84550000}
]

print('COUNTRY POPULATION')

for dict in countries:
    print(dict['name'], dict['population'])