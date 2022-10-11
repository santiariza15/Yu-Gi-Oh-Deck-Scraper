from timeit import default_timer
import grequests
from bs4 import BeautifulSoup

decks =[]
links = [f"https://ygoprodeck.com/Forum/search.php?st=0&sk=t&sd=d&sr=posts&author=renren&ch=1000&start={str(counter)}" for counter in range(0, 1000, 10)]

start_time = default_timer()

reqs = (grequests.get(link) for link in links)
resp=grequests.imap(reqs, grequests.Pool(len(links)))

for r in resp:
    soup = BeautifulSoup(r.text, 'lxml')
    url_elements = soup.find_all(id="xpost_link")
    decks.extend(url['href'] for url in url_elements)
print(f"--- {default_timer() - start_time} seconds ---")

textfile = open("decksURLs2.txt", "w")
for element in decks:
    if "?p=" in element:
        textfile.write(element + "\n")