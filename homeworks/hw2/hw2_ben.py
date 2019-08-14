#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:25:45 2019

Title: Homework 2
@author: bennoble
"""
#Create a .csv file with the following information for each petition:
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

#Create the csv writer
with open('hw2_ben.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('title', 'date', 'issues1', 'issues2', 'issues3', 'signatures'))
  writer.writeheader()
# Create an empty dictionary for each petition entry
  petition = {}
# The petition site has for pages, so I begin by indexing by each page
  for i in range(5):
# Parse the specific page using the index i 
    url = "https://petitions.whitehouse.gov/?page={}".format(i)
    main_page = urllib.request.urlopen(url)
    parsed_main = BeautifulSoup(main_page.read())
# Find all h3 tags — these contain the individual petitions
    h3_tags = parsed_main.find_all('h3')
# Within those h3 tags, find all a tags — these contain the links to each 
# petition page
    for j in h3_tags:
      a_tags = j.find_all('a')
      for tags in a_tags:
# Take each href tag in the a tags (these are the petition links) and 
# concatenate them with the main petition URL. Then parse each individual 
# petition page.
        petition_url = "https://petitions.whitehouse.gov/" + tags['href']
        petition_page = urllib.request.urlopen(petition_url)
        parsed_petition = BeautifulSoup(petition_page.read())
# Find the first h1 tag, which is the petition title. Save it in the dictionary
# as the title
        petition['title'] = parsed_petition.find('h1').get_text()
# Find the first h4 tag which is the author and date
        date = parsed_petition.find('h4')
# These h4 tags follow a standard format of 'created by author on date', so I use the 
# re package to extract only the date (and discard the author portion) then save
# the dates in the date column
        pattern = re.compile('on (.+$)')
        try:
          petition['date'] = pattern.findall(date.get_text()).pop()
# At least one of these petitions is missing a date, so if the date is missing 
# and the script returns an IndexErorr, so I replace it with NA
        except IndexError:
          petition['date'] = 'NA'
# Issues are held within a div tag within the specific class below
        issue_tags = parsed_petition.find('div', {'class' : 'field field-name-field-petition-issues field-type-taxonomy-term-reference field-label-hidden tags'})
# The h6 tags contain the specific issues. There can be a max of of three issues
# but some petitions have only one or two. Python scrapes the first one and 
# adds it to the issue1 column, then if it runs into IndexError (implying that 
# there is no tag), it treats it as NA in the issue2 or issue3 column. Otherwise
# it adds the issue to the appropriate column
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
# Signatures are held within in the unique class signatures-number. I extract 
# the number of petitions, however they have commas which would be annoying if 
# we were going to use this data in R. Therefore, I delete the commas before 
# adding the number to the signature column
        sigs = parsed_petition.find('span', {'class' : 'signatures-number'}).get_text()
        petition['signatures'] = sigs.replace(',','')
        writer.writerow(petition)
