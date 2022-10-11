import pandas as pd
from collections import Counter
import requests
import json

df = pd.read_csv('YGOCardIDs.csv')
cards_int = df['IDs'].tolist()
cards = list(map(str, cards_int))
with open('decks.json', 'r') as f:
  decks = json.load(f)

cards_dict = dict(Counter(cards))
for key, value in decks.items():
  count = 0
  temp = dict(Counter(value))
  length = sum(temp.values())
  cards_done = {}
  for key2, value2 in temp.items():
    if key2 in cards_dict:    
      if cards_dict[key2] >= value2:
        count += value2
        cards_done[key2] = f"{str(value2)}/{str(value2)}"
      else:
        count += value2 - cards_dict[key2]
        cards_done[key2] = f"{str(value2 - cards_dict[key2])}/{str(value2)}"
    elif key2.isnumeric():
      cards_done[key2] = f"0/{str(value2)}"
  if count > 20:
    print(key + ": " + str(count) + " / " + str(length))
    for key3, value3 in cards_done.items():
      URL = f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={str(key3)}'
      page = requests.get(URL).json()
      print(page["data"][0]['name'] + ": " + value3)
    print(" ------------------------------ \n")