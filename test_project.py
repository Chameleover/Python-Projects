from bs4 import BeautifulSoup
import requests
import re


def main():
    kaldata_beauty = get_kaldata_articles()
    kaldata_links = convert_beauty_to_links(kaldata_beauty)

    kaldata_dict = {}
    for i, articles in enumerate(kaldata_links):
        kaldata_dict[kaldata_beauty[i].get_text()] = kaldata_links[i]
    #print(kaldata_dict.values())
    print(check_for_keywords(kaldata_dict))

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



class NewsArticle:
    '''Class for each article

    Processes the article according to the newspaper. Extracts articles, which includes required keywords

    '''

    def __init__(self, url):
        self.url = url


    def request_url(self):
        return requests.get(self.url)


    def extract_content(self):
        content = self.request_url().content
        parsed_content = BeautifulSoup(content, 'html.parser')
        return parsed_content

def check_for_keywords(article_dict):
    '''
    Checks given article dictionary values (links) if they contain given keywords are passed in from file
    :param article_dict:
    :return:
    '''

    base_url = list(article_dict.values())[0]
    article = NewsArticle(base_url)
    if "kaldata" in base_url:
        article_content = article.extract_content().find('div', class_='td-post-content tagdiv-type')
    else:
        print(f"ERROR: {base_url} does not exist in the database!")
    return article_content.text


    # r = requests.get(base_url)
    # if "kaldata" in base_url:
    #     soup = BeautifulSoup() # find('div', class_='td-post-content tagdiv-type')
    # soup = BeautifulSoup(r.text, 'html.parser')
    # return soup.text

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