import requests
import csv
from bs4 import BeautifulSoup as bs

cities = {}

try: 
  r = requests.get('https://www.shaya.com.tr/tr/magazalarimiz/?topZone=32')
  soup = bs(r.content, 'html.parser')
  data = soup.find('table', {'class':"generalTable"})
  data = data.find_all('tr')[1:]
  for i in data:
    nodes = i.find_all('td')
    city = nodes[2].text

    if city in cities:
      cities[city] += 1
    else:
      cities[city] = 1

except:
  print("An exception occurred")

# sort cities according to their values
cities = dict(sorted(cities.items(), key=lambda item: item[1], reverse=True))

for city in cities:
  with open('./datasets/starbucks.txt', 'a') as f:
    f.write(city + ' ' + str(cities[city]) + '\n')

with open('./datasets/starbucks.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerow(['City', 'Count'])
  for key, value in cities.items():
    writer.writerow([key, value])