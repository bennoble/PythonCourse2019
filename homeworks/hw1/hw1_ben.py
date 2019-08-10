"""
Created on Wed Aug  7 14:50:25 2019
Title: Homework 1
Author: Ben Noble
"""

# Preamble
import random
import datetime

# Time function returns current time which is used in the .history() function
def time():
  return "%d:%d" % (datetime.datetime.now().hour, datetime.datetime.now().minute) 

# Overdraft printout informs user when they attempt to overdraft their account
overdraft = "Overdraft: Insufficient Funds. Transaction has been terminated."

# Portfolio class takes no arguments but automatically sets cash balance to 0
# and creates empty lists for stocks, mutual funds, and transaction history.
class Portfolio():
  def __init__(self):
    self.cash = 0 # client's starting cash value
    self.stock_list = {"symbol": [], "shares" : [], "stock" : []} #empty stock list
    self.mf_list = {"symbol": [], "shares" : [], "mf" : []} # empty mutual fund list
    self.hist = []

# Defining the print output of the portfolio object—the key complication is the 
# the fact that dictionaries don't print share: symbol (they print [shares], [symbols])
  def __str__(self):
# Create the lists for printouts
    stock_printout = []
    mf_printout = []
# For each stock symbol, create a new list entry that reads stock_symbol: stock_share
    for i in self.stock_list["symbol"]:
      stock_ind = self.stock_list["symbol"].index(i)
      stock_printout.append("%s: %s" % (self.stock_list["shares"][stock_ind], i))
# For each mutual fund symbol, create a new list entry that reads
# mutual_fund_symbol: mutual_fund_share
    for i in self.mf_list["symbol"]:
      mf_ind = self.mf_list["symbol"].index(i)
      mf_printout.append("%s: %s" % (self.mf_list["shares"][mf_ind], i))
# Print out full portfolio
    return "You have: \n Cash: $%.2f \n Stocks: %s \n Mutual Funds: %s" % (self.cash, ', '.join(stock_printout), ', '.join(mf_printout))

# Allows user to deposit money into their account  
  def addCash(self, money):
    self.cash += money
# Appends transaction record to history list
    self.hist.append(time() + " Deposited $%d" % (money))
    print(self)

# Allows user to withdraw money from their account. If they attempt to overdraw
# the operation aborts.
  def withdrawCash(self, money):
# If user attempts to overdraw their account, the function terminates
    if self.cash - money < 0:
      return overdraft
# Deducts requested cash and records transaction 
    else:  
      self.cash -= money
      self.hist.append(time() + " Withdrew $%s" % (money))
      print(self)
    
  def buyStock(self, shares, stock):
# Check to ensure stock is an integer value. If not, abort.
    if float(shares).is_integer() == False:
      return "Error. Stocks can only be purchased as whole units."
# Check to ensure sufficient funds to make the purchase. If not, abort.
    else:
      if self.cash - stock.price * shares < 0:
        return overdraft
      else:
# If the stock is already in the users portfolio, add shares (rather than create
# a duplicate item)
        if stock.symbol in self.stock_list["symbol"]:
          ind =self.stock_list["symbol"].index(stock.symbol)
          self.stock_list["shares"][ind] += shares
# If this is a new stock, add the symbols and shares to the list
        else:
          self.stock_list["stock"].append(stock)
          self.stock_list["shares"].append(shares)
          self.stock_list["symbol"].append(stock.symbol)
# Deducts cash and records transaction 
        self.cash -= stock.price * shares
        self.hist.append(time() + " Purchased %s shares of %s for $%s each" % (shares, stock.symbol, stock.price))
      print(self)

  def sellStock(self, symb, shares):
# If the user attempts to sell a stock they do not own, abort
    if symb not in self.stock_list["symbol"]:
      return "Error. You do not own any shares of %s" % (symb)
# Next, check to see if the user is trying to sell more shares than they own,
# if so, abort.
    elif symb in self.stock_list["symbol"]:
      ind = self.stock_list["symbol"].index(symb)
      stock =  self.stock_list["stock"][ind]
      if self.stock_list["shares"][ind] - shares < 0:
        return "Insufficient shares. Transaction has been terminated."
      else:
# Deduct shares from the account; if the user sells all shares, remove the stock
# entry from their account
        self.stock_list["shares"][ind] = round(self.stock_list["shares"][ind] - shares, 2)
        if self.stock_list["shares"][ind] == 0:
          self.stock_list["shares"].pop(ind)
          self.stock_list["symbol"].pop(ind)
# Draw the sale price to two decimals, tell the user the price per share
        sale_price = round(random.uniform(stock.price * .5, stock.price * 1.5), 2)
        print("The sale price is %s per share" % (sale_price))
# Adds cash and records transaction 
        self.cash += sale_price * shares
        self.hist.append(time() + " Sold %s shares of %s for $%s each" % (shares, stock.symbol, sale_price))
      print(self)
  
  def buyMutualFund(self, shares, mf):
# Check to ensure sufficient funds to make the purchase. If not, abort.
    if self.cash - 1 * shares < 0:
      return overdraft
    else: 
# If the mutual fund is already in the users portfolio, add shares 
# (rather than create a duplicate item)
      if mf.symbol in self.mf_list["symbol"]: 
        ind = self.mf_list["symbol"].index(mf.symbol)
        self.mf_list["shares"][ind] += shares
      else:
# Otherwise, add symbol and shares to the mutual fund list, then take cash 
# from the account and record history.
        self.mf_list["mf"].append(mf)
        self.mf_list["shares"].append(shares)
        self.mf_list["symbol"].append(mf.symbol)
      self.cash -= 1 * shares
      self.hist.append(time() + " Purchased %s shares of %s for $%s each" % (shares, mf.symbol, 1))
    print(self)
  
  def sellMutualFund(self, symb, shares):
# If the mutual fund selected is not in the mutual fund list, abort.
    if symb not in self.mf_list["symbol"]:
      return "Error. You do not own any shares of %s" % (symb)
# Check to ensure the user is not going to sell more shares than they own. If
# so, abort.
    elif symb in self.mf_list["symbol"]:
      ind = self.mf_list["symbol"].index(symb)
      if self.mf_list["shares"][ind] - shares < 0:
          return "Insufficient shares. Transaction has been terminated."
      else:
# Deduct the shares they want to sell from the mutual fund list
        self.mf_list["shares"][ind] = round(self.mf_list["shares"][ind] - shares, 2)
# If they sell all their shares, remove the symbol and shares from their list
        if self.mf_list["shares"][ind] == 0:
            self.mf_list["shares"].pop(ind)
            self.mf_list["symbol"].pop(ind)
# Determine the sale price rounded to two decimals
        sale_price = round(random.uniform(0.9, 1.2), 2)
# Tell the the user the sale price per share
        print("The sale price is %s per share" % (sale_price))
# Add the sale price * shares to their cash balance and record history.
        self.cash += sale_price * shares
        self.hist.append(time() + " Sold %s shares of %s for $%s each" % (shares, symb, sale_price))
    print(self)

# History function prints full transaction history, but also allows user to 
# request only the last num transactions
  def history(self, num = None):
    if num == None:
      num = len(self.hist)
    print('\n'.join(self.hist[-num:]))

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

# Testing      
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Prints out cash == 300.50
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s, updates cash to 200.50
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT", updates cash to 190.2
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT", updates cash to 188.2
print(portfolio) # prints portfolio readout
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT, adds cash approx $3 to 191.2 and deducts 3 shares of BRT from 10.3 to 7.3
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH, adds cash approx $20 to 211.29 and deducts 1 share of HFH from 5 to 4
portfolio.withdrawCash(50) #Removes $50 to approx 161.29
portfolio.history() # prints transaction history
