from timeit import default_timer
import grequests
from bs4 import BeautifulSoup
import json
import requests

decks = {}
deck_id = 0

with open('decksURLs.txt', 'r') as f:
    links = [line.strip() for line in f]

start_time = default_timer()

reqs = (grequests.get(link) for link in links)
resp=grequests.imap(reqs, grequests.Pool(len(links)))

for r in resp:
    soup = BeautifulSoup(r.text, 'lxml')
    child = soup.find(class_ = "fas fa-download")
    if hasattr(child, 'find_parent'):
        link = child.find_parent('a')['href']
        title = soup.find(class_ = "entry-title").text.replace("\n", "")
        date = soup.find(class_ = "entry-date published").text
        decks[deck_id] = {'title': title, 'deck': requests.get(link).text.splitlines(), 'date': date}
        print(f"{title} done")
        deck_id += 1

print(f"--- {default_timer() - start_time} seconds ---")
print(f'{deck_id} decks found')

with open('decks.json', 'w') as file:
    file.write(json.dumps(decks))