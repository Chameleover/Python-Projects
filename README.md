
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
add ignore case on keywords comparison

This is a python project for CS50P. It's main purpose is to scrape predefined news websites, gather articles by keywords and send them to user by demand.
First version will scrape only text-news and will be executed by .. HOW? ..

I used different libraries to perform similar tasks. Firstly I extract web article's urls and titles with BeautifulSoup
constructor from bs4 library. Then I use Article from newspaper library to get only article text. I check the text for
each article for given keywords, and if found a match the article title and url are added to a dict.
This dict is being converted to xlsx file, which is being converted to a html table and sent to given email address.



#What new skills will you need to acquire? What topics will you need to research?
-web scraping; 
-getting article and links from parsed html; 
-converting dict to xlsx;
-converting xlsx to html table; 
-embedding html body in email; 
-send am email;


#In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to 
accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? 
A better outcome? The best outcome?
The deadline is 1 week (15 January). By then I must have a working version of the project, valid for CS50P certificate.
Later I would improve it by adding mobile version, scraping videos as well, etc.