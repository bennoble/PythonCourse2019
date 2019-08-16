#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Homework 3

Created on Fri Aug 16 15:05:19 2019
@author: bennoble
"""

# Preamble
import tweepy
import json
# http://docs.tweepy.org/en/v3.8.0/api.html

twitter = imp.load_source('twit', '/Users/bennoble/Dropbox/Ben/Keys/start_twitter.py')
api = twitter.client

wustl = api.get_user('WUSTL')
wustl.followers_count

wustl_1 = api.followers(wustl.id, count = 1)
[f.screen_name for f in wustl_1]

json.loads(wustl_1)
