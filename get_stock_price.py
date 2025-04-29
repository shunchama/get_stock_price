import subprocess
import sys
required_packages = ["yfinance", "matplotlib", "pandas"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import yfinance as yf
#import datetime
#mport pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt


#define lists
index_list=[
    "^N225",#日経平均
    "JPY=X"#ドル円
]
owning_list=[
    "4755.T","7201.T","9432.T","9501.T","141A.T"
]
check_list=[
    "7011.T","7012.T","7013.T","7014.T"
]


def get_ticker_info(ticker):
    stock=yf.Ticker(ticker)
    if stock!=None:
        return stock.info
    else:
        print("[err] ticker_info not found")
        return None

def get_cur_price(ticker):
    info=get_ticker_info(ticker)
    if info.get("regularMarketPrice")!=None:
        return info.get("regularMarketPrice")
    else:
        print("[err] cur_price not found")
        return None

def get_name(ticker):
    info=get_ticker_info(ticker)
    if(info.get("longName")!=None):
        return info.get("longName") or info.get("shortName")
    else:
        print("[err] name not found")
        return None

def get_prev_close(ticker):
    info=get_ticker_info(ticker)
    if(info.get("previousClose")!=None):
        return info.get("previousClose")
    else:
        print("[err] prev_close not found")
        return None

def get_price(ticker):
    cur_price=0.0
    prev_close=0.0
    change=0.0
    change_percentage=0.0
    #info=get_ticker_info(ticker)
    cur_price=get_cur_price(ticker)
    prev_close=get_prev_close(ticker)
    name=get_name(ticker)

    if cur_price!=None and prev_close!=None:
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

def get_volume(ticker):
    info=get_ticker_info(ticker)
    if(info.get("volume")!=None):
        return info.get("volume")
    else:
        return "[err]volume not found"

def print_list():
    print_index(index_list)
    print_price(owning_list)
    print_price(check_list)

def read_list():
    print("index_list={}".format(index_list))
    print("owning_list={}".format(owning_list))
    print("check_list={}".format(check_list))

def wait_command():
    command=[
        "print_list(defined_list)",
        "print_index",
        "get+(in:ticker).T",
        "read_list",
        "exit"
    ]
    print("*********************************\ncommand_list: {}\n*********************************".format(command))
    while True:
        print("command: ",end="")
        c=input()
        if c=="print_list":
            print_list()
        elif c=="print_index":
            print_index(index_list)
        elif c=="get":
            print("enter the ticker: ",end="")
            num=input()+".T"
            name=[num]
            print_price(name)
        elif c=="read_list":
            read_list()
        elif c=="exit":
            return
        else:
            print("[err]command not found, plz retype")

def main():
    wait_command()

if __name__=="__main__":
    main()