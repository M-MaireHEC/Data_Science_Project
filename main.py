
#coding: utf-8
#Using throughout the project the documentations of all libraries.
# #The links to libraries documentation can be found in the Bibliography.md file.

# Check and install dependencies
import setup
setup.check_dependencies()

# Importing required libraries
import yfinance as yf
import pandas as pd
from pathlib import Path
import numpy as np


#Asking what tickers to monitor. Automatically removes duplicates and ignores case sensitivity. Allows commas, spaces or semicolons as separators.
def get_tickers() ->list:
    result_tickers = []
    b = True

    while b:
        tickers = input("Please provide the tickers you want to monitor. Commas, spaces or semicolons can be used as separators. \nExample: AAPL, MSFT; GOOGL TSLA MSFT AMZN \n")
        separators = [',', ';', ' ']

        for separator in separators:
            tickers = tickers.replace(separator, ',')

        tickers = tickers.split(',')


        for ticker in tickers:
            ticker = ticker.upper()
            if ticker not in result_tickers:
                result_tickers.append(ticker)
        while True:
            add = input("Would you like to add another ticker? Y/N: ")
            if add.upper() == 'Y':
                b = False
                break
            elif add.upper() == 'N':
                b = True
                break
            else:
                print("Invalid input. Please try again.")

    return result_tickers

#Checking if the ticker exists on Yahoo Finance. Helps avoiding unnecessary errors later on.
def check_ticker(tickers : list) ->list:
    valid_tickers = []
    for ticker in tickers:
        result = yf.Ticker(ticker).info
        if result["trailingPegRatio"] == None:
            print("Invalid ticker:", ticker)
            print("Ticker removed from the list.")
        else:
            valid_tickers.append(ticker)
    return valid_tickers

#ask interval for price data retrieval
def get_interval() -> str:
    while True:
        valid_intervals = ['1wk', '1mo', '1y', '5y', '10y', 'max']
        result = input(f"To what interval should we base our estimation? {valid_intervals}:\n")
        if result.lower().replace(" ","") in valid_intervals:
            return result.lower().replace(" ", "")
        else:
            print("Invalid input. Please try again.")

#Retrieve price data for the given tickers and interval. Store in CSV files named after the ticker to avoid unnecessary repeated downloads.
#Important distinction in the data retrieval. The close price is in reality the adjusted close price, which takes into account dividends and stock splits. This was checked by comparing adjusted close price on Yahoo Finance website and the close price retrieved by yfinance library.
def get_price_data(tickers:list, interval:str)-> None:
    #inspired by pandas documentation : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    for ticker in tickers:
        filepath = Path(f"Data_Output/{ticker}.csv")
        filepath.parent.mkdir(parents=True, exist_ok=True)
        stock = yf.Ticker(ticker)
        prices = stock.history(period=interval)
        prices.to_csv(filepath)

#Opens required csv files and calculates returns based over adjusted closing prices.
def calculate_return_close(tickers:list) -> None:
    for ticker in tickers:
        filepath = Path(f"Data_Output/{ticker}.csv")
        prices = pd.read_csv(filepath)
        prices['Return'] = prices['Close'].pct_change()
        prices.to_csv(filepath, index=False)

#Return daily volatility over the period as standard deviation of returns.
def calculate_volatility(tickers:list) -> int:
    for ticker in tickers:
        filepath = Path(f"Data_Output/{ticker}.csv")
        prices = pd.read_csv(filepath)
        volatility = prices['Return'].std()
        return(volatility)


#Retrieve industry information to become factor in regression analysis.
def get_industry(tickers: list) -> str:
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        infos = stock.info
        industry = infos.get("industry", "0")
        return industry

def get_earnings_history(tickers: list) -> pd.DataFrame:
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        earnings = stock.earnings_history
    return earnings

#Get S&P500 data that is considered as "market" for CAPM
def get_market_data(interval:str) -> None:
    market = ["SPX"]
    get_price_data(market, interval)

#Get all caps S&P 500 for multifactor model
def get_small_medium_large_data(interval:str) -> None:
    market = ["^SP600", "^MID", "^GSPC" ]
    get_price_data(market)





if __name__ == "__main__":
    #debug section
    #print(get_tickers())
    #print(check_ticker(["MSFT","sjhd","sahjdh"]))
    #print(get_interval())
    #print(get_earnings_history(["MSFT"]))
    #get_market_data("max")


    pass