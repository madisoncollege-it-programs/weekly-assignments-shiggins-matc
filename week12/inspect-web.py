#!/usr/bin/env python3

import requests,bs4

res = requests.get('http://notpurple.com')
res.raise_for_status()

myHTML = bs4.BeautifulSoup(res.text,features="html.parser")


print(myHTML.title.text)
titles = myHTML.select('a')
print(titles)
