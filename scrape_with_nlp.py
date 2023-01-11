import nltk
from newspaper import Article

# get the article
url = 'https://www.kaldata.com/it-%d0%bd%d0%be%d0%b2%d0%b8%d0%bd%d0%b8/%d1%86%d0%b5%d0%bb%d0%b8%d1%8f%d1%82-%d1%81%d0%b2%d1%8f%d1%82-%d1%81%d0%b5-%d0%bf%d0%be%d0%b1%d1%8a%d1%80%d0%ba%d0%b0-%d0%bf%d0%be-chatgpt-%d1%85%d0%b0%d0%b9%d0%b4%d0%b5-%d0%b4%d0%b0-%d0%b3%d0%be-403568.html'

article = Article(url)

# Do some NLP
article.download()
article.parse()
# nltk.download('punkt')
# article.nlp()

# Get the article text
print(article.text)