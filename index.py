import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/', timeout=10)
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')  # Get the title and link of the story
subtext = soup.select('.subtext')  # Get the subtext of each story


# New function to sort the articles based on points recieved

def sort_articles(hnlist):
    # From the dictionary we choose to sort the list by votes
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def topstories_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        story = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            # Only getting stories with points 100 or greater
            if points > 99:
                hn.append({'story': story, 'link': href, 'votes': points})
    return sort_articles(hn)


pprint.pprint(topstories_hn(links, subtext))
