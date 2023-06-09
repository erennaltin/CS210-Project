import csv


data = []
with open('./datasets/gdp.txt', 'r') as f:
  data = f.readlines()[1:]
  for idx, item in enumerate(data):
    item = item.strip()
    nodes = item.split(' ')
    data[idx] = nodes

with open('./datasets/gdp.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['city', 'count($)'])
  for item in data:
    # conver CITY to City
    item[0] = item[0].title()
    writer.writerow(item)


