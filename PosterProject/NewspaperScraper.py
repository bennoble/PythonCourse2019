#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Newspaper Scraping

Created on Wed Aug 14 13:57:25 2019
@author: bennoble
"""
# Preamble
from bs4 import BeautifulSoup
import urllib.request
import csv 
import unicodedata
import datetime

MO_searchURL = "https://www.stltoday.com/search/?f=html&q=mike+parson&d1=2018-04-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o=000"
MO_search = urllib.request.urlopen(MO_searchURL)
parsed_MO = BeautifulSoup(MO_search.read())
#parsed_MO
h3 = parsed_MO.find_all('h3', {'class' : 'tnt-headline'})

h3[2].find('a')['href']

parsed_MO.find('time').get_text()

day = datetime.datetime("Jul 1, 2019")
print(day.strftime("%b"))
datetime.strptime(day, "%m/%d/%y")

datetime.datetime.strptime(day, "%b %d, %Y")

with open('gov_newspapers.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('first name', 'last name', 'state', 'newspaper', 'article headline', 'date', 'url', 'body text'))
  writer.writeheader()
  news = {}
  for i in range(6):
    mo_url = "https://www.stltoday.com/search/?f=html&q=mike+parson&d1=2018-04-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o={}00".format(i)
    mo_search = urllib.request.urlopen(mo_url)
    parsed_mo = BeautifulSoup(mo_search.read())
    h3_tag = parsed_mo.find_all('h3', {'class' : 'tnt-headline'})
    for headline in range(2, len(h3_tag)):
      news['first name'] = "Mike"
      news['last name'] = 'Parsons'
      news['state'] = 'MO'
      news['newspaper'] = 'St. Louis Post Dispatch'
      news['article headline'] = unicodedata.normalize('NFKD', h3_tag[headline].get_text()).strip()
      news['url'] = 'https://www.stltoday.com' + h3_tag[headline].find('a')['href']
      writer.writerow(news)
    
  