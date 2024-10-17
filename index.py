import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/', timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline a')  # Get the title and link of the story
votes = soup.select('.score')  # Get the points from each story


def topstories_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        story = links[idx].getText()
        href = links[idx].get('href', None)
        # condition as some stories may not have any points
        if idx < len(votes):
            # replace so that we are only retrieving an integer so we can order them
            points = votes[idx].getText().replace(' points', '')
        else:
            points = '0'
        hn.append({'story': story, 'links': href, 'votes': points})
    return hn


print(topstories_hn(links, votes))
