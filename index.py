import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/', timeout=10)
res2 = requests.get('https://news.ycombinator.com/?p=2', timeout=10)

html_text = res.text + res2.text
soup = BeautifulSoup(html_text, 'html.parser')

links = soup.select('.titleline > a')
subtext = soup.select('.subtext')


def sort_articles(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def topstories_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        story = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'story': story, 'link': href, 'votes': points})
    return sort_articles(hn)


pprint.pprint(topstories_hn(links, subtext))
