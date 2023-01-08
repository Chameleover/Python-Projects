from bs4 import BeautifulSoup
import requests
import re


def main():
    kaldata_beauty = get_kaldata_articles()

    kaldata_links = convert_beauty_to_links(kaldata_beauty)

class Newspaper:
    '''Class for each newspaper included in the web scraper

    Returns parsed html page by passing it to the BeatufulSoup constructor. 'html.parser' uses the best available
    parseer. Might be slow if website has way too many articles.


    '''
    def __init__(self, url):
        self.url = url


    def get_content(self):
        return requests.get(self.url)


    def parse_articles(self):
        articles = self.get_content().content
        beauty = BeautifulSoup(articles, 'html.parser')
        return beauty

def get_kaldata_articles():

    kaldata_url = "https://www.kaldata.com/"

    kaldata = Newspaper(kaldata_url)

    # kaldata article parameters: 'h3', class_='entry-title td-module-title'
    kaldata_news = kaldata.parse_articles().find_all('h3', class_='entry-title td-module-title')
    return kaldata_news


def convert_beauty_to_links(beauty: list):
    '''
    Accepts list of bs4 string, including all html5 parameters, cleans them up and returns a list with links and
    headlines
    :param beauty:
    :return: list of all articles
    '''
    list_of_articles = []

    for link in beauty:
        # convert from bs4 class to string
        link = str(link)
        matches = re.search(r"(https?://(?:www\.)?.?[^\"]+)", link, re.IGNORECASE)
        parsed = matches.group(1)
        list_of_articles.append(parsed)

    if len(list_of_articles) < 1:
        print("WARNING: Website has 0 articles.")

    return list_of_articles



if __name__ == "__main__":
    main()