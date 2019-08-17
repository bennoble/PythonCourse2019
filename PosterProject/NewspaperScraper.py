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
import time

MO_searchURL = "https://www.stltoday.com/search/?f=html&q=mike+parson&d1=2018-04-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o=000"
MO_search = urllib.request.urlopen(MO_searchURL)
parsed_MO = BeautifulSoup(MO_search.read())
#parsed_MO
h3 = parsed_MO.find_all('h3', {'class' : 'tnt-headline'})

h3[2].find('a')['href']

parsed_MO.find('time').get_text()
article = urllib.request.urlopen("https://www.stltoday.com/opinion/editorial/editorial-nothing-says-pro-life-like-prosecuting-the-victim-for/article_e73e9589-d39f-5d1a-8294-4507c0380218.html")
parsed_article = BeautifulSoup(article.read())
parsed_article.find('time').get_text()
parsed_article.find('div', {'itemprop' : 'articleBody'}).get_text().strip()

# MO - St. Louis Post Dispatch
with open('gov_newspapers.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('first name', 'last name', 'state', 'newspaper', 'article headline', 'date', 'url', 'body text'))
  writer.writeheader()
  news = {}
  for i in range(6):
    mo_url = "https://www.stltoday.com/search/?f=html&q=mike+parson&d1=2018-04-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o={}00".format(i)
    mo_search = urllib.request.urlopen(mo_url)
    parsed_mo = BeautifulSoup(mo_search.read())
    h3_tag = parsed_mo.find_all('h3', {'class' : 'tnt-headline'})
    for headline in range(len(h3_tag)):
      time.sleep(2)
      try: 
        news['first name'] = "Mike"
        news['last name'] = 'Parsons'
        news['state'] = 'MO'
        news['newspaper'] = 'St. Louis Post Dispatch'
        news['article headline'] = unicodedata.normalize('NFKD', h3_tag[headline].get_text()).strip()
        news['url'] = 'https://www.stltoday.com' + h3_tag[headline].find('a')['href']
        article = urllib.request.urlopen(news['url'])
        parsed_article = BeautifulSoup(article.read())
        news['date'] = parsed_article.find('time').get_text()
        news['body text'] = parsed_article.find('div', {'itemprop' : 'articleBody'}).get_text().strip()
        writer.writerow(news)
      except urllib.error.HTTPError:
        pass

# NH - New Hampshire Union Leader
with open('gov_newspapers_test.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('first name', 'last name', 'state', 'newspaper', 'article headline', 'date', 'url', 'body text'))
  writer.writeheader()
  news = {}
  for i in range(22):
    nh_url = "https://www.unionleader.com/search/?f=html&q=Chris+Sununu&d1=2017-01-01&d2=2019-07-01&s=start_time&sd=desc&l=100&t=article&nsa=eedition&app%5B0%5D=editorial&o={}00".format(i)
    nh_search = urllib.request.urlopen(nh_url)
    parsed_nh = BeautifulSoup(nh_search.read())
    h3_tag = parsed_nh.find_all('h3', {'class' : 'tnt-headline'})
    for headline in range(len(h3_tag)):
      #time.sleep(2)
      try: 
        news['first name'] = "Chris"
        news['last name'] = 'Sununu'
        news['state'] = 'NH'
        news['newspaper'] = 'New Hampshire Union Leader'
        news['article headline'] = unicodedata.normalize('NFKD', h3_tag[headline].get_text()).strip()
        news['url'] = 'https://www.unionleader.com' + h3_tag[headline].find('a')['href']
        article = urllib.request.urlopen(news['url'])
        parsed_article = BeautifulSoup(article.read())
        news['date'] = parsed_article.find('time').get_text()
        news['body text'] = parsed_article.find('div', {'itemprop' : 'articleBody'}).get_text().strip()
        writer.writerow(news)
      except urllib.error.HTTPError:
        pass


# Will need selenium
vt_url = "https://www.burlingtonfreepress.com/search/phil%20scott/"
vt_search = urllib.request.urlopen(vt_url)
parsed_vt = BeautifulSoup(vt_search.read())
parsed_vt

# MD — Baltimore Sun
with open('gov_newspapers_test.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('first name', 'last name', 'state', 'newspaper', 'article headline', 'date', 'url', 'body text')))
  writers.writeheader()
  news = {}
    i = 1
  for 
    md_url = 'https://www.baltimoresun.com/search/larry%20hogan/100-y/story/date/{}/'.format(i)
    md_search = urllib.request.urlopen(md_url)
    parsed_md = BeautifulSoup(md_search.read())
    headline = parsed_md.find_all('div', {'class' : 'h7'})
    for i in range

i = 1
while True:
  md_url = 'https://www.baltimoresun.com/search/larry%20hogan/100-y/story/date/{}/'.format(i)
  md_search = urllib.request.urlopen(md_url)
  parsed_md = BeautifulSoup(md_search.read())
  headline = parsed_md.find_all('div', {'class' : 'h7'})
  for h7 in headline:
#    news['headline']
    link_out = h7.find('a')['href'] 
    article_url = 'https://www.baltimoresun.com' + link_out
    article_search = urllib.request.urlopen(article_url)
    parsed_article = BeautifulSoup(article_search.read())
    date = parsed_article.find_all('span', {'class' : 'timestamp timestamp-article'})[1].get_text()
    print(date)
    if 'Aug 01' in date:
      break
  i += 1

i=1
md_url = 'https://www.baltimoresun.com/search/larry%20hogan/100-y/story/date/{}/'.format(i)
md_search = urllib.request.urlopen(md_url)
parsed_md = BeautifulSoup(md_search.read())
headline = parsed_md.find_all('div', {'class' : 'h7'})
for h7 in headline:
#    news['headline']
  link_out = h7.find('a')['href'] 
  article_url = 'https://www.baltimoresun.com' + link_out
  article_search = urllib.request.urlopen(article_url)
  parsed_article = BeautifulSoup(article_search.read())
  date = parsed_article.find_all('span', {'class' : 'timestamp timestamp-article'})[1].get_text()
  print(date)
  if 'Aug 01' in date:
    break

for i in headline:
  print(i.get_text())
