
#coding: utf-8
#Using throughout the project the documentations of all libraries.
# #The links to libraries documentation can be found in the Bibliography.md file.

# Check and install dependencies
import setup
setup.check_dependencies()

# Importing required libraries
import yfinance as yf

#Asking what tickers to monitor. Automatically removes duplicates and ignores case sensitivity. Allows commas, spaces or semicolons as separators.
def get_tickers():
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

if __name__ == "__main__":
    print(get_tickers())