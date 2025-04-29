import datetime
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def get_ticker_info(ticker):
    stock=yf.Ticker(ticker)
    return stock.info

def get_cur_price(ticker):
    info=get_ticker_info(ticker)
    if info.get("regularMarketPrice")!=None:
        return info.get("regularMarketPrice")
    else:
        return "not found"

def get_name(ticker):
    info=get_ticker_info(ticker)
    if(info.get("longName")!=None):
        return info.get("longName") or info.get("shortName")
    else:
        return "not found"

def get_prev_close(ticker):
    info=get_ticker_info(ticker)
    if(info.get(previousClose)!=None):
        return info.get("previousClose")
    else:
        return "not found"

def get_price(ticker):
    info=get_ticker_info(ticker)
    cur_price=get_cur_price(ticker)
    prev_close=info.get("previousClose")
    name=get_name(ticker)
    
    if cur_price==None or prev_close==None:
        return None,None,None,None
    
    change=cur_price-prev_close
    change_percentage=(change/prev_close)*100
    return name,cur_price,change,change_percentage

def print_price(ticker_list):
    for i in ticker_list:
        name,cur,diff,percentage=get_price(i)
        print("[{}]{}".format(i,name))
        symbol=""
        if diff>=0:
            symbol="+"
        else:
            symbol="-"
        print("        {}({}{:.2f},{}{:.2f}%)".format(cur,symbol,abs(diff),symbol,abs(percentage)))
    print("*********************************")

def print_index(index_list):
    print("*********************************")
    print_price(index_list)
    print("*********************************")

def main():
    index_list=[
        "^N225",#日経平均
        "JPY=X"#ドル円
    ]
    owning_list=[
        "4755.T","7201.T","9432.T","9501.T"
    ]
    list=[
        "7011.T","7012.T","7013.T","7014.T"
    ]
    
    print_index(index_list)
    print_price(owning_list)
    print_price(list)

if __name__=="__main__":
    main()