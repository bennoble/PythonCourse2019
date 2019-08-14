#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Governor Approval Data from Morning Consult

Created on Tue Aug 13 10:51:11 2019
@author: bennoble
"""

# Preamble
from bs4 import BeautifulSoup
import urllib.request
import csv 
import json

# Grabbing the morning consult governor rankings page 
mc_web = "https://morningconsult.com/governor-rankings-q2-19/"
mc_page = urllib.request.urlopen(mc_web)

# Parsing the page
parsed_page = BeautifulSoup(mc_page.read())

# Finding the scripts
scripts = parsed_page.find_all('script', {"type" : "text/javascript"})

# Finding the specific script that contains the governor data
for i in range(len(scripts)):
  for j in scripts[i]:
    if "var mc_senators" in j:
      app_data = scripts[i]

# Get the text of the governor text and convert it to a python dictionary
app_text = app_data.get_text()
pdict = json.loads(app_text[35:-12])

# Writing the csv file
with open('gov_approval_Q12017toQ219.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ('first name', 'last name', 'party', 'state', 'state abbr', 'quarter', 'approval', 'disapproval'))
  writer.writeheader()
  gov = {}
# First subset by the dictionary keys (which are the governors full names)
  for name in pdict.keys():
# Then subset by each quarter we have for them
    for q in range(len(pdict[name]['trend_dates'])):
      gov['first name'] = pdict[name]["info"]["first_name"]
      gov['last name'] = pdict[name]["info"]["last_name"]
      gov['party'] = pdict[name]["info"]["party"]
      gov['state'] = pdict[name]['info']['state']
      gov['state abbr'] = pdict[name]['info']['state_abbr']
      gov['quarter'] = pdict[name]['trend_dates'][q]
      gov['approval'] = pdict[name]['trend_data'][0]['data'][q]
      gov['disapproval'] = pdict[name]['trend_data'][1]['data'][q]
      writer.writerow(gov)