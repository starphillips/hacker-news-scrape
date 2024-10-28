<h1> Hacker News Top Stories Scraper </h1>

This is a Python script that scrapes top stories from Hacker News and filters the results based on the number of votes. Only stories with 100 or more votes are included in the output.

The script fetches the front page and the second page of Hacker News, parses the HTML, and then sorts the stories by the number of votes in descending order.

<h2> Features </h2>

- Fetches stories from the first two pages of Hacker News.
- Filters out stories with fewer than 100 points.
- Sorts stories by the number of votes in descending order.

<h2> Requirements </h2>
- Python 3.6+
- Required packages listed in `requirements.txt` (install using `pip install -r requirements.txt`)

<h2> Usage </h2>
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/starphillips/hacker-news-scrape.git
   cd hacker-news-scrape




