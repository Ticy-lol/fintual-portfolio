

""" defincion de stock """
class Stock:
    def __init__(self, ticker):
        self.ticker=ticker
    
    def get_market_value(self):
        """Simular respuesta de API"""
        if self.ticker=='AAPL':
            return 100
        elif self.ticker=='META':
            return 200
        elif self.ticker=='GOOGLE':
            return 10
        elif self.ticker=='ARAUCO':
            return 20
        return 0

class Portafolio:
    def __init__(self, target_allocation,stocks):
        self.stock_inventory= stocks
        self.target_allocation = target_allocation
            
    def rebalance(self):
        buy_sell_stocks=[]
        total_amount=0
        """ recorre los stocks que tengo: calculo el monto total de dinero que tengo y verifico si existen en la nueva estrategia,
            si no existen, tengo que vender todo de ese stock.
        """
        for ticker, ticker_amount in self.stock_inventory.items():
            stock=all_stocks[ticker]
            value=self.target_allocation.get(ticker)
            total_amount+=stock.get_market_value()*ticker_amount
            if(value is None or value == 0):
                buy_sell_stocks.append({'ticker':stock.ticker,'amount':ticker_amount,'operation':'sell'})
                
        print(f'total_amount {total_amount}')
        
        """ recorro la nueva estrategia: para saber que tengo que comprar y/o vender"""
        for ticker, percent in self.target_allocation.items():
            stock=all_stocks[ticker]
            value=self.stock_inventory.get(ticker)
            """ validacion para casos en que mi diccionario no tenga el stock definido """
            if(value is None):
                quantity_to_buy=total_amount/stock.get_market_value()*percent
                buy_sell_stocks.append({'ticker':stock.ticker,'amount':quantity_to_buy,'operation':'buy'})
                
            else:
                """ casos en donde el stock existe en mi diccionario """
                ticker_total_amount=total_amount*percent
                my_ticker_amount=self.stock_inventory[ticker]
                amount=my_ticker_amount*stock.get_market_value()
                
                if(amount<ticker_total_amount):
                    quantity_to_buy=(ticker_total_amount-amount)/stock.get_market_value()
                    buy_sell_stocks.append({'ticker':stock.ticker,'amount':quantity_to_buy,'operation':'buy'})
                    

                if(amount>ticker_total_amount):
                    quantity_to_sell=(amount-ticker_total_amount)/stock.get_market_value()
                    buy_sell_stocks.append({'ticker':stock.ticker,'amount':quantity_to_sell,'operation':'sell'})
                    
                    
        return buy_sell_stocks

        

        

all_stocks={"META":Stock("META"),'AAPL':Stock("AAPL") ,'GOOGLE':Stock("GOOGLE"), 'ARAUCO':Stock('ARAUCO')}

 
""" estrategias de rebalance: se asume que la suma tiene que ser 1 (100%) """
strategy = {all_stocks['META'].ticker: 0.5, all_stocks['AAPL'].ticker:0.5} 
strategy2 = {all_stocks['GOOGLE'].ticker: 0.5,all_stocks['ARAUCO'].ticker: 0.5} 
strategy3 = {all_stocks['META'].ticker: 0.9,all_stocks['ARAUCO'].ticker: 0.1} 

my_stocks={ all_stocks['META'].ticker :20 , all_stocks['AAPL'].ticker:80}  #4000 en META y 8000 en AAPL

my_portfolio= Portafolio(strategy3,my_stocks)

print(my_portfolio.rebalance())













