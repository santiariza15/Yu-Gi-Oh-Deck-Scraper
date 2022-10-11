import pandas as pd
from collections import Counter
import requests

df = pd.read_csv('YGOCardIDs.csv')
cards_int = df['IDs'].tolist()
cards = list(map(str, cards_int))
with open('Floowandereeze.ydk', 'r') as f:
  deck = f.read().splitlines()

cards_dict = dict(Counter(cards))
deck_dict = dict(Counter(deck))
count = 0
cards_done = {}
length = sum(deck_dict.values())
for key, value in deck_dict.items():
  if key in cards_dict:
    if cards_dict[key] >= value:
      count += value
      cards_done[key] = f"{str(value)}/{str(value)}"
    else:
      count += value - cards_dict[key]
      cards_done[key] = f"{str(value - cards_dict[key])}/{str(value)}"
  elif key.isnumeric():
    cards_done[key] = f"0/{str(value)}"
print(f"{str(count)} / {str(length)}")
for key2, value2 in cards_done.items():
  URL = f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={str(key2)}'
  page = requests.get(URL).json()
  print(page["data"][0]['name'] + ": " + value2)