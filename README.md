
# YOUR PROJECT TITLE

#### Video Demo:  <URL HERE>
#### Description:
TODO:
make class NewsPaper.
create object for each website
create class NewsArticle and create object for each article
store news article in iterable data structure, and iterate over them to check for keywords
if keyword found, add the article to a new dictionary.
send the output to given email
error handling
test cases

This is a python project for CS50P. It's main purpose is to scrape predefined news websites, gather articles by keywords and send them to user by demand.
First version will scrape only text-news and will be executed by .. HOW? ..

I used different libraries to perform similar tasks. Firstly I extract web article's urls and titles with BeautifulSoup
constructor from bs4 library. Then I use Article from newspaper library to get onlty article text. I check the text for
each article for given keywords, and if found at least #5 matches the article title and url are added to a dict.
This dict is being formatted and sent to given email address.



#What new skills will you need to acquire? What topics will you need to research?
I need to research web scraping, find a user-friendly way to execute the program, find a friendly way to store the output, and possibly find how to run it on a mobile device.

#If working with one or two classmates, who will do what?
#In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
The deadline is 1 week (15 January). By then I must have a working version of the project, valid for CS50P certificate.
Later I would improve it by adding mobile version, scraping videos as well, etc.