import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/', timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')  # Get the title and link of the story
# Swap to subject as there will always be an equal amount of subtext to stories
subtext = soup.select('.subtext')


def topstories_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        story = links[idx].getText()
        href = links[idx].get('href', None)
        # From subtext I can select score
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'story': story, 'link': href, 'votes': points})
    return hn


print(topstories_hn(links, subtext))
