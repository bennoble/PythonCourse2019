#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 3

Created on Fri Aug 16 15:05:19 2019
@author: bennoble
"""

# Preamble
import tweepy
import time
# http://docs.tweepy.org/en/v3.8.0/api.html

twitter = imp.load_source('twit', '/Users/bennoble/Dropbox/Ben/Keys/start_twitter.py')
api = twitter.client

wustl = api.get_user('WUSTL')

wustl.followers_count
wustl_1 = api.followers(wustl.id, count = 1)
[f.screen_name for f in wustl_1]
[f.followers_count for f in wustl_1]
[f.statuses_count for f in wustl_1]

wustl_followers = api.followers(wustl.id, count = 10)
[f.screen_name for f in wustl_followers]
name = []
follower_num = []
status_num = []

for f in wustl_followers:
  name.append(f.screen_name)
  follower_num.append(f.followers_count)
  status_num.append(f.statuses_count)
  


[f.screen_name for f in wustl_followers]
[f.followers_count for f in wustl_followers]
[f.statuses_count for f in wustl_followers]



wustl.friends_count
wustl_1f = api.friends(wustl.id, count = 1)
[f.screen_name for f in wustl_1f]


follower_name = []
follower_num = []
follower_status_num = []

for fol in tweepy.Cursor(api.followers, id = 'WUSTL').items(5):
  follower_name.append(fol.screen_name)
  follower_num.append(fol.followers_count)
  follower_status_num.append(fol.statuses_count)
    
for i in range(len(follower_name)):
  print('name %s, num fol %s, num status %s' % (follower_name[i], follower_num[i], follower_status_num[i]))
  
ind = follower_num.index(min(follower_num))
follower_name[ind]
follower_num
