#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:50:25 2019

Title: Homework 1
Author: Ben Noble
"""

# Creating the portfolio
class Portfolio():
  def __init__(self, name, cash):
    self.name = name #client's name
    self.cash = cash # client's starting cash value
    self.stock = [] #empty stock list
    self.mf = [] # empty mutual fund list
  
  def __str__(self):
    return "%s has: \n Cash: $%s \n Stocks: %s \n Mutual Funds: %s" % (self.name, self.cash, self.stock, self.mf)

  def check_bal(self):
    return "%s has a balance of $%d" % (self.name, self.cash)
  
  def deposit(self, money):
    self.cash += money
    return self.check_bal()
  
  def withdraw(self, money):
    if self.cash - money < 0:
      return "Error. Insufficient Funds."
    else:
      self.cash -= money
      return self.check_bal()
  
class FinancialInstruments():
  def __init__(self, symbol, price):
      self.symbol = symbol
      self.price = price
  
  def __str__(self):
    return "%s : %d" % (self.symbol, self.price)

class Stock(FinancialInstrument):
  
class MututalFund(FinancialInstrument):
    
  
bob = Portfolio("Bob", 50) #Creates a new portfolio
print(bob)
bob.check_bal()
bob.deposit(80)
bob.check_bal()
bob.withdraw(40)
bob.withdraw(100)
bob.check_bal()
