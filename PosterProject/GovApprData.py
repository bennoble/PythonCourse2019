#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:51:11 2019

@author: bennoble
"""

from bs4 import BeautifulSoup
import urllib.request
import csv 
import unicodedata
import re

mc_web = "https://morningconsult.com/governor-rankings-q2-19/"
mc_page = urllib.request.urlopen(mc_web)
mc_page

parsed_page = BeautifulSoup(mc_page.read())
scripts = parsed_page.find_all('script', {"type" : "text/javascript"})

for i in range(len(scripts)):
  for j in scripts[i]:
    if "var mc_senators" in j:
      app_data = scripts[i]

for i in range(len(app_data)):
  print(app_data[i])
  
print(app_data.values())
app_data

baker = re.search('first_name(.+?)Q2"]}', app_data.get_text()).group()
print(baker)

pattern = re.compile('{"info":(.+?)Q2"]}')
data = pattern.findall(app_data.get_text())
data[0]

fnames = []
lnames = []
for i in range(len(data)):
  fnames.append(re.findall(r'"first_name":"(.+?)","last_name"', data[i]).pop()) 
  lnames.append(re.findall(r'"last_name":"(.+?)","rank"', data[i]).pop())

fnames
lnames

appr = []

for i in range(len(data)):
  appr.append(re.findall(r'"data":(.+?)},', data[i]).pop()) 

appr

re.findall(r'"data":(.+?)},', data[0])
  