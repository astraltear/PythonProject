# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin
from scrapy.selector import Selector

def fetch_page(url):
    r = requests.get(url)
    return r.text

def talk_links_from_listpage(url):
    html = fetch_page(url)
    sel = Selector(text=html)
    talk_links = sel.css('.talk-link .media__message a::attr(href)').extract()
    talk_links = [urljoin(url, talk_link) for talk_link in talk_links]
    return talk_link
    
'''
with open('sample.html','wb') as f:
    html = fetch_page("http://www.ted.com/talks/browse?page=2")
    #print(html)
    f.write(html.encode('utf-8'))
'''

page_link = "http://www.ted.com/talks/browse?page=2"
print( talk_links_from_listpage(page_link))
    
print("END")