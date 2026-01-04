import yfinance as yf
from backend.yfinance.lookup.lookup_objects import *

def lookup(text):
    if not text: 
        return False
    else:
        lookup = yf.Lookup(text).all

        lookup_clean = lookup.where(lookup.notnull(), None)
        lookupDict = {}

        for symbol, row in lookup_clean.iterrows():
            lookupDict[symbol] = Lookup.model_validate(row.to_dict())

        if lookupDict == {}:
            return False
        else:
            return lookupDict
