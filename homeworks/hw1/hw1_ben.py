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
    self.stock_list = {"symbol": [], "buy price" : [], "shares" : []} #empty stock list
    self.mf_list = {} # empty mutual fund list
  
  def __str__(self):
    return "%s has: \n Cash: $%s \n Stocks: %s \n Mutual Funds: %s" % (self.name, self.cash, self.stock_list, self.mf_list)

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
  
  def fin_withdraw(self, shares, stock):
    if self.cash - stock.price * shares < 0:
      return "Error. Insufficient Funds."
    else:
      self.cash -= stock.price * shares
  
  def buy_stock(self, shares, stock):
    self.stock_list["shares"].append(shares)
    self.stock_list["symbol"].append(stock.symbol)
    self.stock_list["buy price"].append(stock.price)
    #self.fin_withdraw() How does this take the withdrawl function to keep things DRY?

  
class FinancialInstrument():
  def __init__(self, price, symbol):
      self.price = price
      self.symbol = symbol
  
  def __str__(self):
    return "%s : %d" % (self.symbol, self.price)

class Stock(FinancialInstrument):
  pass

class MututalFund(FinancialInstrument):
  pass    
  
bob = Portfolio("Bob", 50) #Creates a new portfolio
s = Stock(20, "HFH")
q = Stock(40, "ABC")
print(s)
bob.buy_stock(5, s)
bob.buy_stock(2, q)
print(bob)

print(bob)
bob.check_bal()
bob.deposit(80)
bob.check_bal()
bob.withdraw(40)
bob.withdraw(100)
bob.check_bal()
