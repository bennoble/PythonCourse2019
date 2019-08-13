#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:25:45 2019

Title: Homework 2
@author: bennoble
"""
#Create a .csv fil
le with the following information for each petition:
# -Title
# -Published date 
# -Issues tags
# -Number of signatures

# Preamble
from bs4 import BeautifulSoup
import urllib.request
import csv 
import unicodedata
import re

with open('hw2_ben.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('title', 'date', 'issues1', 'issues2', 'issues3', 'signatures'))
  writer.writeheader()
  petition = {}
  for i in range(4):
    url = "https://petitions.whitehouse.gov/?page={}".format(i)
    main_page = urllib.request.urlopen(url)
    parsed_main = BeautifulSoup(main_page.read())
    h3_tags = parsed_main.find_all('h3')
    for j in h3_tags:
      a_tags = j.find_all('a')
      for tags in a_tags:
        petition_url = "https://petitions.whitehouse.gov/" + tags['href']
        petition_page = urllib.request.urlopen(petition_url)
        parsed_petition = BeautifulSoup(petition_page.read())
        petition['title'] = parsed_petition.find('h1').get_text()
        date = parsed_petition.find('h4')
        pattern = re.compile('on (.+$)')
        try:
          petition['date'] = pattern.findall(date.get_text()).pop()
        except IndexError:
          petition['date'] = 'NA'
        issue_tags = parsed_petition.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
        h6_tags = issue_tags.find_all('h6')
        petition['issues1'] = unicodedata.normalize('NFKD', h6_tags[0].get_text())
        try:  
          petition['issues2'] = unicodedata.normalize('NFKD', h6_tags[1].get_text())
        except IndexError:
          petition['issues2'] = 'NA'
        try:  
          petition['issues3'] = unicodedata.normalize('NFKD', h6_tags[2].get_text())
        except IndexError:
          petition['issues3'] = 'NA'
        sigs = parsed_petition.find('span', {'class' : 'signatures-number'}).get_text()
        petition['signatures'] = sigs.replace(',','')
        writer.writerow(petition)
