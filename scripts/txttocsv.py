import csv

def turkish_lower(s):
    s = s.replace('I', 'ı').replace('İ', 'i')
    return s.lower()

data = []
with open('./datasets/highschool_education_rate_according_meb.txt', 'r') as f:
  data = f.readlines()[1:]
  for idx, item in enumerate(data):
    item = item.strip()
    nodes = item.split(' ')
    data[idx] = nodes

with open('./datasets/highschool_education_rate_according_meb.csv', 'w',  encoding='utf-8') as f:
  f.write('city,school_rate\n')
  # writer = csv.writer(f)
  # writer.writerow(['city', 'count($)'])
  for item in data:
      itemInfo = ','.join(item)
      f.write(itemInfo + '\n')


