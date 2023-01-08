import re

beauty = '<h3 class="entry-title td-module-title"><a href="https://www.kaldata.com/%d1%81%d0%be%d1%84%d1%82%d1%83%d0%b5%d1%80/tapinradio-89656.html" rel="bookmark" title="TapinRadio 2.15.95.9">TapinRadio 2.15.95.9</a></h3>'

matches = re.search(r"(https?://(?:www\.)?.?[^\"]+)", beauty, re.IGNORECASE)
parsed = matches.group(1)

print(parsed)
