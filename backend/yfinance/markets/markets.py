import yfinance as yf
from backend.yfinance.markets.markets_objects import *

def getMarketEurope (): 
    
    europe = yf.Market("EUROPE")
    # Wir erstellen erst ein sauberes Dictionary
    print(europe)
    
    marketEU = Market.model_validate(europe.status)
    #print(europe.summary)   

    exchanges = {}
    for key in europe.summary:
        json_exchange = europe.summary[key]
        exchange = Exchange(**json_exchange)
        exchanges[key] = exchange
    
    exchangeKeys = exchanges.keys()
    for key in exchangeKeys:
        print(exchanges.get(key))
    return marketEU

