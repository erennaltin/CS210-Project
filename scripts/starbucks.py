import requests
import csv
from bs4 import BeautifulSoup as bs
import string

def turkish_lower(s):
    s = s.replace('I', 'ı').replace('İ', 'i')
    return s.lower()


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

with open('./datasets/starbucks.csv', 'w', encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['city', 'starbucks count'])
  for key, value in cities.items():
    key = turkish_lower(key)
    key = key.title()
    
    writer.writerow([key, value])

