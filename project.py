from bs4 import BeautifulSoup
import requests
import re
from newspaper import Article
import csv
from functionality.convert_dict_to_excel import xlsx_to_html, create_hyperlinks_file
from functionality.send_email import email_new


def main():
    kaldata_beauty = get_kaldata_articles()
    kaldata_links = convert_beauty_to_links(kaldata_beauty)

    kaldata_dict = create_dict_of_articles(kaldata_links, kaldata_beauty)

    # extract only articles, containing required keywords
    news_dict = check_for_keywords(kaldata_dict)
    # convert dict to xlsx file
    create_hyperlinks_file(news_dict)
    # covert the xlsx file to html file
    html_table = xlsx_to_html()

    email_new(html_table)


class Newspaper:
    """Class for each newspaper included in the web scraper

    Returns parsed html page by passing it to the BeatufulSoup constructor. 'html.parser' uses the best available
    parseer. Might be slow if website has way too many articles.
    """

    def __init__(self, url):
        self.url = url

    def get_content(self):
        return requests.get(self.url)

    def parse_articles(self):
        articles = self.get_content().content
        beauty = BeautifulSoup(articles, 'html.parser')
        return beauty


def get_kaldata_articles():
    """
    scrape web articles from given web address.
    class_='entry-title td-module-title' is exported from kaldata website, which includes only articles.
    :return: parsed html list of all kaldata articles of bs4 class
    """
    kaldata_url = "https://www.kaldata.com/"
    kaldata = Newspaper(kaldata_url)
    kaldata_news = kaldata.parse_articles().find_all('h3', class_='entry-title td-module-title')

    return kaldata_news


def convert_beauty_to_links(beauty: list):
    """
    Accepts list of bs4 class, including all html5 parameters, cleans them up and returns a list with links and
    headlines, using python regex.
    :param beauty:
    :return: list of all articles
    """
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


def create_dict_of_articles(website_links, website_beauty):
    website_dict = {}
    for i, articles in enumerate(website_links):
        website_dict[website_beauty[i].get_text()] = website_links[i]

    return website_dict


def check_for_keywords(article_dict):
    """
    Checks given article dictionary values (links) if they contain given keywords are passed in from file
    and store title:link in another dictionary
    :param article_dict:
    :return:
    """
    # Create an empty dict to store accepted articles
    dict_of_article_content = {}

    # Iterate over all articles 1 by 1
    for article_url in article_dict.values():

        # Extract only article content from the web page
        article = Article(article_url)
        article.download()
        article.parse()
        article_to_list = list(article.text.split(' '))
        keywords = get_keywords()

        # Store each article, containing a keyword in a new dict
        if any(word in keywords for word in article_to_list):
            print(f"Article: \"{article.title}\" stored")
            dict_of_article_content[article.title] = article_url

    return dict_of_article_content


def get_keywords():
    file = open("docs/article_keywords.csv", "r")
    data = list(csv.reader(file))
    file.close()
    # list(csv.reader(file)) stores list within the 0 element of a list. So we need to return the 0 element
    return data[0]


if __name__ == "__main__":
    main()
