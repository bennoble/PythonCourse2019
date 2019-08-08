#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:50:25 2019

Title: Homework 1
Author: Ben Noble
"""

# Loading packages
import random

# Creating the portfolio class which allows the user to input their name and 
# starting cash value. Code automatically creates empty lists for stocks and
# mutual funds
class Portfolio():
  def __init__(self, name, cash):
    self.name = name #client's name
    self.cash = cash # client's starting cash value
    self.stock_list = {"symbol": [], "shares" : []} #empty stock list
    self.mf_list = {"symbol": [], "shares" : []} # empty mutual fund list

# Defining the print output of the portfolio object  
  def __str__(self):
    return "%s has: \n Cash: $%.2f \n Stocks: %s \n Mutual Funds: %s" % (self.name, self.cash, self.stock_list, self.mf_list)

# Allows user to deposit money into their account  
  def deposit(self, money):
    self.cash += money
    print(self)

# Allows user to withdraw money from their account. If they attempt to overdraw
# the operation aborts.
  def withdraw(self, money):
    if self.cash - money < 0:
      return "Error. Insufficient Funds."
    else:
      self.cash -= money
      print(self)
  
  def buy_stock(self, shares, stock):
# Check to ensure stock is an integer value. If not, abort.
    if float(shares).is_integer() == False:
      return "Error. Stocks can only be purchased as whole units."
# Check to ensure sufficient funds to make the purchase. If not, abort.
    else:
      if self.cash - stock.price * shares < 0:
        return "Error. Insufficient Funds."
# Adds symbol and shares to the stock list, then takes cash from the account.
      else:
        self.stock_list["shares"].append(shares)
        self.stock_list["symbol"].append(stock.symbol)
        self.cash -= stock.price * shares
      return self.stock_list
  
  def buy_mutual_fund(self, shares, mf):
# Check to ensure sufficient funds to make the purchase. If not, abort.
    if self.cash - 1 * shares < 0:
      return "Error. Insufficient Funds."
# Adds symbol and shares to the mutual fund list, then takes cash from the account.
    else:
      self.mf_list["shares"].append(shares)
      self.mf_list["symbol"].append(mf.symbol)
      self.cash -= 1 * shares
    return self.mf_list
  
  def sell_mutual_fund(self, shares, mf):
# If the mutual fund selected is not in the mutual fund list, abort.
    if all(i != mf.symbol for i in self.mf_list["symbol"]):
      return "Error. You do not own any shares of %s." % (mf.symbol)
# For the mutual fund selected that matches the mutual fund in the list...
    for i in self.mf_list["symbol"]:
      if i == mf.symbol:
# capture the index value of that symbol in the mutual fund list.
        ind = self.mf_list["symbol"].index(i)
# Using that index, find that same index in shares. If user attempts to sell
# more shares than they have, abort.
        if self.mf_list["shares"][ind] - shares < 0:
          return "Error. Insufficient shares."
        else:
# Deduct the shares they want to sell from the mutual fund list
          self.mf_list["shares"][ind] = round(self.mf_list["shares"][ind] - shares, 2)
# If they sell all their shares, remove the symbol and shares from their list
          if self.mf_list["shares"][ind] == 0:
            self.mf_list["shares"].pop(ind)
            self.mf_list["symbol"].pop(ind)
# Determine the sale price rounded to two digits
          sale_price = round(random.uniform(0.9, 1.2), 2)
# Tell the the user the sale price per share
          print("The sale price is %s per share" % (sale_price))
# Add the sale price * shares to their cash balance.
          self.cash += sale_price * shares
    print(self)

# Define financial instrument class which has a price and symbol  
class FinancialInstrument():
  def __init__(self, price, symbol):
      self.price = price
      self.symbol = symbol

# define print function for financial instruments which displays symbol: price  
  def __str__(self):
    return "%s: %d" % (self.symbol, self.price)

# Stocks inheret all aspects of financial instruments
class Stock(FinancialInstrument):
  pass

# Mutual funds are automatically created with a sale price of 1 but otherwise
# inheret all other aspects of financial instruments 
class MutualFund(FinancialInstrument):
  def __init__(self, symbol):
      FinancialInstrument.__init__(self, 1, symbol)   
  
bob = Portfolio("Bob", 50) #Creates a new portfolio
hfh = Stock(20, "HFH")
abc = Stock(40, "ABC")
brt = MutualFund("BRT")
xyz = MutualFund("XYZ")
ben = MutualFund("BEN")
print(hfh)
print(brt)
print(brt)

bob.buy_mutual_fund(10.3, brt)
bob.buy_mutual_fund(3.2, xyz)
print(bob)

bob.sell_mutual_fund(2.2, xyz)

#random.uniform(.9, 1.2)

#bob.buy_stock(5, hfh)
#bob.buy_stock(2, abc)
#bob.buy_stock(2, hfh)
#print(bob)

#print(bob)
#bob.check_bal()
bob.deposit(80)
#bob.check_bal()
#bob.withdraw(40)
#bob.withdraw(100)
#bob.check_bal()

#bob.buy_stock(1.2, hfh)

#float(1.0).is_integer()
