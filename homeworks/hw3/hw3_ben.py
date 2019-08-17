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
import imp
# http://docs.tweepy.org/en/v3.8.0/api.html

# Loading the API
twitter = imp.load_source('twit', '/Users/bennoble/Dropbox/Ben/Keys/start_twitter.py')
twitter
api = twitter.client





follows_name = []
follows_num = []
follows_status_num = []

# Capturing @WUSTL's follows
def follows():
  for fol in tweepy.Cursor(api.friends, id = 'WUSTL').items():
    try:
# Get the name, number of followers, and number of tweets of each user 
# @WUSTL follows and append to list
      follows_name.append(fol.screen_name)
      follows_num.append(fol.followers_count)
      follows_status_num.append(fol.statuses_count)
# I set the API to wait_on_rate_limit = True so this is probably not necessary
# But I am paranoid!
    except tweepy.TweepError:
      time.sleep(15 * 60)
      continue
# Pause for 30s if there's a connection error
    except ConnectionError:
      time.sleep(30)
      continue
# Call the followers function
follows()  

len(follows_name) # Check to ensure we've captures all follows: 866

# Among those who @WUSTL follows, who has the greatest number of followers?
follows_name[follows_num.index(max(follows_num))] ## It's Twitter with...
max(follows_num) ## 56,511,292 followers

# Among those who @WUSTL follows, who has the most tweets by category?
def follows_tweets():
  layman = 0
  expert = 0
  celeb = 0
  name_layman = None
  name_expert = None
  name_celeb = None
  for i in range(len(follows_status_num)):
    if follows_status_num[i]  < 100:
      if layman < follows_status_num[i]:
        layman = follows_status_num[i]
        name_layman = follows_name[i]
      else:
        pass
    if follows_status_num[i] > 100 and follows_status_num[i] < 1000:
      if expert < follows_status_num[i]:
        expert = follows_status_num[i]
        name_expert = follows_name[i]
    if follows_status_num[i] > 1000:
      if celeb < follows_status_num[i]:
        celeb = follows_status_num[i]
        name_celeb = follows_name[i]
  print('%s: %s' % (name_layman, layman))
  print('%s: %s' % (name_expert, expert))
  print('%s: %s' % (name_celeb, celeb))
      
follows_tweets() # WUSTLdigital: 97 // CollegeCEOs: 994 // nytimes: 368674
    
    
laymen['tweet num'].append(follows_status_num[i])
laymen['name'].append(follows_name[i])

follows_name[619]  

laymen['tweet num'][619]
laymen['name']

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


follows_name = []
follows_num = []
follows_status_num = []

def follows():
  for fol in tweepy.Cursor(api.friends, id = 'WUSTL').items():
    try:
      follows_name.append(fol.screen_name)
      follows_num.append(fol.followers_count)
      follows_status_num.append(fol.statuses_count)
    except tweepy.TweepError:
      time.sleep(15 * 60)
      continue
    except ConnectionError:
      time.sleep(30)
      continue

follows()  

len(follows_name)

follows_name[803:807]
follows_name[follows_num.index(max(follows_num))]

follows_name1 = follows_name
len(follows_name)

for fol in tweepy.Cursor(api.friends, id = 'WUSTL').items(5):
    while True:  
      try:
        #api = twitter.client
        print(fol.screen_name)
      except tweepy.RateLimitError:
        print("no")
      except tweepy.TweepError:
        print("tweep")

  
  
for i in range(len(follows_name)):
  print('name %s, num fol %s, num status %s' % (follows_name[i], follows_num[i], follows_status_num[i]))

len(follows_name)
follows_name[285]

for i in follows_name:
  print(follows_name.index(i - 1))
  
for i in follows_name:
  print(i[1]-1)
  
follows_name.index('nocmgr')
limit = api.rate_limit_status()
limit['resources']['friends']

for i in limit["resources"]["followers"].keys():
	print(limit["resources"]["followers"][i])
    
    
for fol in tweepy.Cursor(api.friends, id = 'WUSTL').items():
  follows_name.append(fol.screen_name)
  follows_num.append(fol.followers_count)
  follows_status_num.append(fol.statuses_count)

