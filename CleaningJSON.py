import json

with open('decks.json', 'r') as f:
  decks = json.load(f)

main = []
extra = []
side = []
x = 0
list_of_types = [main, extra, side]

deck = decks["0"]["deck"]
if "created" in deck[0]:
    deck.pop(0)
for element in deck:
    if "main" in element:
        x = 0
    if "extra" in element:
        x = 1
    if "side" in element:
        x = 2
    list_of_types[x].append(element)

