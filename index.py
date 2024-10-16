import requests
from bs4 import BeautifulSoup


# Pulling inital HTML from Hacker News
res = requests.get('https://news.ycombinator.com/')
bs4 = BeautifulSoup(res.text, 'html.parser')

# Checking bs4
print('Website in HTML format')
print(soup)

print('Specific data inside body html tags')
print(soup.body)

# Print div tags
print(soup.find_all('div'))
