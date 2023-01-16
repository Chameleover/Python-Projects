
# Web Newscraper

### by Filip Andonov, Bulgaria, Blagoevgrad

#### Video Demo:  https://youtu.be/s4nZ6pNX5j0
#### Description: 
This is a python project created for CS50P. It's main purpose is to scrape predefined news websites, gather articles by 
keywords and send them to user by demand.

I used different libraries to perform similar tasks, to enrich my knowledge. Firstly I extract web article's urls and 
titles with BeautifulSoup constructor from bs4 library. Then I use Article from newspaper library to get only article 
text. I check the text for each article for given keywords, and if found a match the article title and url are added to 
a dict. This dict is being converted to xlsx file, which is being converted to a html table and sent to given email address.
send_email.py sends an email using office356 server. sender's email & password, as well as receiver are stored in
creds.py file, for security purpose.

P.S Keywords are stored in csv file, and must be written manually before project's execution.

P.P.S in test_project.py can't be implemented hardcoded test cases as we used to do in the harvard homework projects, so
for now the file is with empty functions. Test cases will be implemented later

#### TODO:
- make class NewsPaper.
- create object for each website
- store news article in iterable data structure, and iterate over them to check for keywords
- if keyword found, add the article to a new dictionary.
- convert dictionary to html table, which could look good in email body
- send the output to given email
- error handling
- test cases
- add ignore case on keywords comparison




#### What new skills will you need to acquire? What topics will you need to research?
- web scraping; 
- getting article and links from parsed html; 
- converting dict to xlsx;
- converting xlsx to html table; 
- embedding html body in email; 
- send am email;


#### In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
The deadline is 1 week (15 January). By then I must have a working version of the project, valid for CS50P certificate.
Later I would improve it by adding more websites and a mobile version.


Disclaimer: This project is made to be presented and defended as Harvard CS50 Python Final Project. It is ment only for
educational purposes! Anyone can feel free to copy, alter, add new functionalities to the project. 