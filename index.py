import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/', timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline a')  # Get the title and link of the story


def topstories_hn(links):
    hn = []
    for idx, item in enumerate(links):
        story = links[idx].getText()
        href = links[idx].get('href', None)
        # append into dictionary
        hn.append({'story': story, 'links': href})
    return hn


print(topstories_hn(links))
