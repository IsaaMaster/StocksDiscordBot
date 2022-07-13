from logging import exception
from stocksHelper import getPrice


startingCash = 10000

class Player:
    def __init__(self, cash, stocks, user) -> None:
        self.cash = cash
        self.stocks = stocks
        self.user = user

    def getPortfolioValue(self):
        return float("%.4f"%(self.cash + self.valueOfStocks()))

    def valueOfStocks(self):
   
        total = int()
        for stock in self.stocks:
            total+= getPrice(stock) * self.stocks[stock]
        return total
    
    def buy(self, stock, amount):
        if (amount < 1):
            raise exception
        price = getPrice(stock)

        if (price*amount > self.cash):
           raise exception
        
        self.cash-=price*amount
        if stock in self.stocks:
            self.stocks[stock]+=amount
        else:
            self.stocks[stock] = amount
        

            

    def sell(self, stock, amount):
        if (amount < 1):
            raise exception
        if (stock not in self.stocks or self.stocks[stock] < amount):
            raise exception
        price = getPrice(stock)
        self.cash+=price*amount
        self.stocks[stock]-=amount
        if (self.stocks[stock] == 0):
            self.stocks.pop(stock)
    
    def getPercentage(self):
        return float("%.4f"%((self.getPortfolioValue() - startingCash)/startingCash*100))



    def __str__(self) -> str:
        text = "Cash: " + str("%.4f"%self.cash) + "\n"
        for stock in self.stocks:
            text += str(stock).upper() + " (" + str(self.stocks[stock])+") @" + str(getPrice(stock)) + "\n"
        return text
    

    
    



