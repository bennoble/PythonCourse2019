#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:50:25 2019

Title: Homework 1
Author: Ben Noble
"""

# Loading packages
import random

# Creating the portfolio
class Portfolio():
  def __init__(self, name, cash):
    self.name = name #client's name
    self.cash = cash # client's starting cash value
    self.stock_list = {"symbol": [], "buy price" : [], "shares" : []} #empty stock list
    self.mf_list = {"symbol": [], "shares" : []} # empty mutual fund list
  
  def __str__(self):
    return "%s has: \n Cash: $%d \n Stocks: %s \n Mutual Funds: %s" % (self.name, self.cash, self.stock_list, self.mf_list)

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
  
 # def fin_withdraw(self, shares, stock):
 #   if self.cash - stock.price * shares < 0:
 #     return "Error. Insufficient Funds."
 #   else:
 #     self.cash -= stock.price * shares
  
  def buy_stock(self, shares, stock):
    if float(shares).is_integer() == False:
      return "Error. Stocks can only be purchased as whole units."
    else:
      if self.cash - stock.price * shares < 0:
        return "Error. Insufficient Funds."
      else:
        self.stock_list["shares"].append(shares)
        self.stock_list["symbol"].append(stock.symbol)
        self.stock_list["buy price"].append(stock.price)
        self.cash -= stock.price * shares
      return self.stock_list
  
  def buy_mutual_fund(self, shares, mf):
    if self.cash - 1 * shares < 0:
      return "Error. Insufficient Funds."
    else:
      self.mf_list["shares"].append(shares)
      self.mf_list["symbol"].append(mf.symbol)
      self.cash -= 1 * shares
    return self.mf_list
  
  def sell_mutual_fund(self, shares, mf):
    for i in self.mf_list["symbol"]:
      if i == mf.symbol:
        ind = self.mf_list["symbol"].index(i)
        if self.mf_list["shares"][ind] - shares < 0:
          return "Error. Insufficient shares."
        else:
          self.mf_list["shares"][ind] -= shares
          sale_price = random.uniform(0.9, 1.2)
          print(sale_price * shares)
        print(self)
  
class FinancialInstrument():
  def __init__(self, price, symbol):
      self.price = price
      self.symbol = symbol
  
  def __str__(self):
    return "%s : %d" % (self.symbol, self.price)

class Stock(FinancialInstrument):
  pass

class MutualFund(FinancialInstrument):
  def __init__(self, symbol):
      FinancialInstrument.__init__(self, 1, symbol)   
  
bob = Portfolio("Bob", 50) #Creates a new portfolio
hfh = Stock(20, "HFH")
abc = Stock(40, "ABC")
brt = MutualFund("BRT")
xyz = MutualFund("XYZ")
print(hfh)
print(brt)
print(brt)

bob.buy_mutual_fund(10.3, brt)
bob.buy_mutual_fund(3.2, xyz)
print(bob)

bob.sell_mutual_fund(2.3, xyz)

#random.uniform(.9, 1.2)

#bob.buy_stock(5, hfh)
#bob.buy_stock(2, abc)
#bob.buy_stock(2, hfh)
#print(bob)

#print(bob)
#bob.check_bal()
#bob.deposit(80)
#bob.check_bal()
#bob.withdraw(40)
#bob.withdraw(100)
#bob.check_bal()

#bob.buy_stock(1.2, hfh)

#float(1.0).is_integer()
