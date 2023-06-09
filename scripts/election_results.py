"""
The url: https://secim2023.cnnturk.com/api/home
The data that will come from the api is the following:
This script will return a json object that contains the following data:

{
    "Adana": "CHP" or "AKP" or "MHP" or "IYI" or "HDP" or "SP" or "DP" or "BBP" or "VP" or "TKP" or "Diger",
    "Adiyaman": "CHP" or "AKP" or "MHP" or "IYI" or "HDP" or "SP" or "DP" or "BBP" or "VP" or "TKP" or "Diger",
    ...
}

"""

import json
import requests
from requests.exceptions import HTTPError

url = "https://secim2023.cnnturk.com/api/home/"

headers = {'Content-Type': 'application/json'}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
else:
    data = response.json()
    party_map = data.get('partyMap')
    provinces = dict()
    for item in party_map:
        winner_name = item.get('winner').get('displayName')
        province_name = item.get('regionName')
        provinces[province_name] = winner_name

    open('../datasets/election_results.json', 'w', encoding='utf-8').write(
        json.dumps(provinces, indent=4, sort_keys=True, ensure_ascii=False))
