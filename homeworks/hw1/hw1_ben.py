"""
Created on Wed Aug  7 14:50:25 2019
Title: Homework 1
Author: Ben Noble
"""

# Preamble
import random
import datetime

def time():
  return "%d:%d" % (datetime.datetime.now().hour, datetime.datetime.now().minute) 

overdraft = "Overdraft: Insufficient Funds. Transaction has been terminated."

# Creating the portfolio class which allows the user to input their name and 
# starting cash value. Code automatically creates empty lists for stocks and
# mutual funds
class Portfolio():
  def __init__(self, name, cash):
    self.name = name #client's name
    self.cash = cash # client's starting cash value
    self.stock_list = {"symbol": [], "shares" : [], "stock" : []} #empty stock list
    self.mf_list = {"symbol": [], "shares" : [], "mf" : []} # empty mutual fund list
    self.hist = []

# Defining the print output of the portfolio object  
  def __str__(self):
    return "%s has: \n Cash: $%.2f \n Stocks: %s: %s \n Mutual Funds: %s: %s" % (self.name, self.cash, self.stock_list["symbol"], self.stock_list["shares"], self.mf_list["symbol"], self.mf_list["shares"])

# Allows user to deposit money into their account  
  def addCash(self, money):
    self.cash += money
    self.hist.append(time() + " Deposited $%d" % (money))
    print(self)

# Allows user to withdraw money from their account. If they attempt to overdraw
# the operation aborts.
  def withdrawCash(self, money):
    if self.cash - money < 0:
      return overdraft
    else:  
      self.cash -= money
      self.hist.append(time() + " Withdrew $%d" % (money))
      print(self)
    
  def buyStock(self, shares, stock):
# Check to ensure stock is an integer value. If not, abort.
    if float(shares).is_integer() == False:
      return "Error. Stocks can only be purchased as whole units."
# Check to ensure sufficient funds to make the purchase. If not, abort.
    else:
      if self.cash - stock.price * shares < 0:
        return overdraft
# Adds symbol and shares to the stock list, then takes cash from the account.
      else:
        self.stock_list["stock"].append(stock)
        self.stock_list["shares"].append(shares)
        self.stock_list["symbol"].append(stock.symbol)
        self.cash -= stock.price * shares
        self.hist.append(time() + " Purchased %d shares of %s for $%d each" % (shares, stock.symbol, stock.price))
      print(self)

  def sellStock(self, symb, shares):
    if symb not in self.stock_list["symbol"]:
      return "Error. You do not own any shares of %s" % (symb)
    elif symb in self.stock_list["symbol"]:
      ind = self.stock_list["symbol"].index(symb)
      stock =  self.stock_list["stock"][ind]
      if self.stock_list["shares"][ind] - shares < 0:
        return overdraft
      else:
        self.stock_list["shares"][ind] = round(self.stock_list["shares"][ind] - shares, 2)
        if self.stock_list["shares"][ind] == 0:
          self.stock_list["shares"].pop(ind)
          self.stock_list["symbol"].pop(ind)
        sale_price = round(random.uniform(stock.price * .5, stock.price * 1.5), 2)
        print("The sale price is %s per share" % (sale_price))
        self.cash += sale_price * shares
        self.hist.append(time() + " Sold %d shares of %s for $%d each" % (shares, stock.symbol, sale_price))
      print(self)
  
  def buyMutualFund(self, shares, mf):
# Check to ensure sufficient funds to make the purchase. If not, abort.
    if self.cash - 1 * shares < 0:
      return overdraft
# Adds symbol and shares to the mutual fund list, then takes cash from the account.
    else:
      self.mf_list["mf"].append(mf)
      self.mf_list["shares"].append(shares)
      self.mf_list["symbol"].append(mf.symbol)
      self.cash -= 1 * shares
      self.hist.append(time() + " Purchased %d shares of %s for $%d each" % (shares, mf.symbol, 1))
    print(self)
  
  def sellMutualFund(self, symb, shares):
# If the mutual fund selected is not in the mutual fund list, abort.
    if symb not in self.mf_list["symbol"]:
      return "Error. You do not own any shares of %s" % (symb)
    elif symb in self.mf_list["symbol"]:
      ind = self.mf_list["symbol"].index(symb)
# For the mutual fund selected that matches the mutual fund in the list....
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
        self.hist.append(time() + " Sold %d shares of %s for $%d each" % (shares, symb, sale_price))
    print(self)

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
      
bob = Portfolio("Bob", 500) #Creates a new portfolio
hfh = Stock(20, "HFH")
abc = Stock(40, "ABC")
brt = MutualFund("BRT")
xyz = MutualFund("XYZ")
ben = MutualFund("BEN")
print(hfh)
print(brt)
print(brt)

bob.buyStock(3, abc)
bob.sellStock("ABC", 1)


bob.history()

bob.buy_stock(50, hfh)

bob.buyMutualFund(10.3, xyz)
bob.sellMutualFund("XYZ", 5)


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
#bob.check_bal()
#bob.withdraw(40)
#bob.withdraw(100)
#bob.check_bal()

#bob.buy_stock(1.2, hfh)

#float(1.0).is_integer()