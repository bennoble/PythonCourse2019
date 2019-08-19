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



######################
# 1A and 1B: Among the followers of @WUSTL, who has the greatest number 
# of total tweets/followers
######################

def followers_comp():
  tweets = 0
  fols = 0
  handle_tweets = None
  handle_fols = None
  i = 0
# For each of @WUSTL's followers...
  for fol in tweepy.Cursor(api.followers, id = 'WUSTL').items():
# Increase the count; print every 1000th i—this just helps me keep track of the
# the function's progress
    i += 1
    if i % 1000 == 0:
      print(i)
    try:
# If the current followers follower count is greater than the existing count,
# replace the existing count with the current count and save that user's name
      if fol.followers_count > fols:
        fols = fol.followers_count
        handle_fols = fol.screen_name
        print(handle_fols)
# If the current followers tweet count is greater than the existing count,
# replace the existing count with the current count and save that user's name
      if fol.statuses_count > tweets:
        tweets = fol.statuses_count
        handle_tweets = fol.screen_name
        print(handle_tweets)
# May not need this since I set the API option to wait on rate limit
    except tweepy.RateLimitError:
      print("Rate Limit hit. Sleeping.")
      time.sleep(15 * 60)
      continue
# Pause for 30s if there's a connection error
    except ConnectionError:
      print("Connection Error. Sleeping.")
      time.sleep(30)
      continue
# Print the winner of each category
  return "Most followers: %s %s. Most tweets: %s %s." % (handle_fols, fols, handle_tweets, tweets)

q1 = followers_comp()
q1 
# Most followers: hootsuite 7,858,471. 
# Most tweets: brontyman 582,447

######################
# 1C and 1D: Among those who @WUSTL follows, who has the greatest number of 
# followers/tweets by category?
######################

follows_name = []
follows_num = []
follows_status_num = []

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
# Call the follows function
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
# For each user I've already collected in the follows_num list...
  for i in range(len(follows_num)):
# If the current user has less than 100 followers, they are a layman
    if follows_num[i] < 100:
# If the current layman has more tweets than the existing layman, replace that
# layman with the current layman and save their name
      if layman < follows_status_num[i]:
        layman = follows_status_num[i]
        name_layman = follows_name[i]
# Elif the current user has between 100 and 1000 followers, they are an expert         
    elif follows_num[i] > 100 and follows_num[i] < 1000:
# If the current expert has more tweets than the existing expert, replace that
# expert with the current expert and save their name
      if expert < follows_status_num[i]:
        expert = follows_status_num[i]
        name_expert = follows_name[i]
# If the current user has more than 1000 followers, they are a celebrity
    elif follows_num[i] > 1000:
# If the current celebrity has more tweets than the existing celebrity, replace that
# celebrity with the current celebrity and save their name
      if celeb < follows_status_num[i]:
        celeb = follows_status_num[i]
        name_celeb = follows_name[i]
# Print the winners in each category        
  print('Layman: %s, %s' % (name_layman, layman))
  print('Expert: %s, %s' % (name_expert, expert))
  print('Celebrity: %s, %s' % (name_celeb, celeb))
      
follows_tweets() # WUSTLdigital: 97 // CollegeCEOs: 994 // nytimes: 368674

######################
# 2A: Among the (laymen and experts) followers of @WUSTLPoliSci and their 
# followers, who has the greatest number of tweets?
######################

def followerfollower():
  wustlps_followerfollower = []
  count = 0
  name = None
  i = 0
# For each follower of @WUSTLPoliSci...
  for fol in tweepy.Cursor(api.followers, 'WUSTLPoliSci').items(2):
# This part counts which user @WUSTLPoliSci follows that I am currently on, 
# just helps me keep track of the function's progress since it takes a while to run
    i += 1
    print(i)
    try:
# I add the follower to the list then go through all the users followers
# and append them to the list
      wustlps_followerfollower.append(fol)
      for folfol in tweepy.Cursor(api.followers, fol.screen_name).items(2):
        wustlps_followerfollower.apend(folfol)
        print('done')
# If there's a connection error, pause for 30s
    except ConnectionError:
      time.sleep(30)
      continue
# For each user on the list with less than 1000 followers... 
  for user in wustlps_followerfollower:
    if user.followers_count < 1000:
# If the user's status count is greater than the current highest count, replace
# the count and the screen name with this user
      if user.statuses_count > count:
        count = user.statuses_count
        name = user.screen_name
# Print the ultimate winner
  return '%s, %s' % (name, count)

q2a = followerfollower()
q2a

######################
# 2B: Among those (laymen and experts) who @WUSTLPoliSci follows and those who 
# they follow, who has the greatest number of tweets?
######################

def followfollow():
  wustlps_followfollow = []
  count = 0
  name = None
  i = 0
# For each user @WUSTLPoliSci follows...
  for fol in tweepy.Cursor(api.friends, 'WUSTLPoliSci').items():
# This part counts which user @WUSTLPoliSci follows that I am currently on, 
# just helps me keep track of the function's progress since it takes a while to run
    i += 1
    print(i)
    try:
# I add the followed user to the list then go through all the users they're
# following and append them to the list
      wustlps_followfollow.append(fol)
      for folfol in tweepy.Cursor(api.friends, fol.screen_name).items():
        wustlps_followfollow.append(folfol)
# If there's a connection error, pause for 30s
    except ConnectionError:
      time.sleep(30)
      continue
# For each user on the list with less than 1000 followers... 
  for user in wustlps_followfollow:
    if user.followers_count < 1000:
# If the user's status count is greater than the current highest count, replace
# the count and the screen name with this user
      if user.statuses_count > count:
        count = user.statuses_count
        name = user.screen_name
# Print the ultimate winner
  return '%s, %s' % (name, count)

q2b = followfollow()
q2b



################### Delete

fol_name1 = follower_name
fol_num1 = follower_num
fol_stat1 = follower_status_num
    
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

for fol in tweepy.Cursor(api.friends, id = 'WUSTL').items(1):
   print(fol)
  
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

test = [1, 4, 7, 9, 2, 3]
ind = None
a = 0
for i in range(len(test)):
  if test[i] < 8:
    if test[i] > a:
      a = test[i]
      ind = i
print(a)
print(ind)  

for item in tweepy.Cursor(api.followers, 'realDonaldTrump').items(2):
	print(item)
    
wustlps = api.get_user('WUSTLPoliSci')
wustlps.followers
wustlps.statuses_count
wustlps.screen_name
dir(wustlps)

def followfollow():
  wustlps_followfollow = []
  count = 0
  name = None
  for fol in tweepy.Cursor(api.friends, 'WUSTLPoliSci').items(2):
    wustlps_followfollow.append(fol)
    for folfol in tweepy.Cursor(api.friends, fol.screen_name).items():
      wustlps_followfollow.append(folfol)
  for user in wustlps_followfollow:
    if user.followers_count < 1000:
      print(user.statuses_count)
      print(user.screen_name)
      if user.statuses_count > count:
        count = user.statuses_count
        name = user.screen_name
  return '%s, %s' % (name, count)

followfollow()


dt_fols = []
for fol in tweepy.Cursor(api.friends, dt.screen_name).items(1):
  dt_fols.append(fol)

dt_fols[0].statuses_count
