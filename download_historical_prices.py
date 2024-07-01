# import os
# from pandas_datareader import data as pdr
# import pandas as pd
# import yfinance as yf

# yf.pdr_override()

# START_DATE = "2003-08-01"
# END_DATE = "2015-01-01"


# def build_stock_dataset(start=START_DATE, end=END_DATE):
#     """
#     Creates the dataset containing all stock prices
#     :returns: stock_prices.csv
#     """

#     statspath = "intraQuarter/_KeyStats/"
#     ticker_list = os.listdir(statspath)

#     # Required on macOS
#     if ".DS_Store" in ticker_list:
#         os.remove(f"{statspath}/.DS_Store")
#         ticker_list.remove(".DS_Store")

#     # Get all Adjusted Close prices for all the tickers in our list,
#     # between START_DATE and END_DATE
#     all_data = pdr.get_data_yahoo(ticker_list, start, end)
#     stock_data = all_data["Adj Close"]

#     # Remove any columns that hold no data, and print their tickers.
#     stock_data.dropna(how="all", axis=1, inplace=True)
#     missing_tickers = [
#         ticker for ticker in ticker_list if ticker.upper() not in stock_data.columns
#     ]
#     print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
#     # If there are only some missing datapoints, forward fill.
#     stock_data.ffill(inplace=True)
#     stock_data.to_csv("stock_prices.csv")


# def build_sp500_dataset(start=START_DATE, end=END_DATE):
#     """
#     Creates the dataset containing S&P500 prices
#     :returns: sp500_index.csv
#     """
#     index_data = pdr.get_data_yahoo("SPY", start=START_DATE, end=END_DATE)
#     index_data.to_csv("sp500_index.csv")


# def build_dataset_iteratively(
#     idx_start, idx_end, date_start=START_DATE, date_end=END_DATE
# ):
#     """
#     This is an alternative iterative solution to building the stock dataset, which may be necessary if the
#     tickerlist is too big.
#     Instead of downloading all at once, we download ticker by ticker and append to a dataframe.
#     This will download data for tickerlist[idx_start:idx_end], which makes this method suitable
#     for chunking data.

#     :param idx_start: (int) the starting index of the tickerlist
#     :param idx_end: (int) the end index of the tickerlist
#     """

#     statspath = "intraQuarter/_KeyStats/"
#     ticker_list = os.listdir(statspath)

#     df = pd.DataFrame()

#     for ticker in ticker_list:
#         ticker = ticker.upper()

#         stock_ohlc = pdr.get_data_yahoo(ticker, start=date_start, end=date_end)
#         if stock_ohlc.empty:
#             print(f"No data for {ticker}")
#             continue
#         adj_close = stock_ohlc["Adj Close"].rename(ticker)
#         df = pd.concat([df, adj_close], axis=1)
#     df.to_csv("stock_prices.csv")


# if __name__ == "__main__":
#     build_stock_dataset()
#     build_sp500_dataset()







import os
import pandas as pd
import yfinance as yf
import pandas_datareader.data as pdr

# Override the default data reader with yfinance
yf.pdr_override()

START_DATE = "2003-08-01"
END_DATE = "2015-01-01"

def build_stock_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing all stock prices
    :returns: stock_prices.csv
    """
    
    statspath = "intraQuarter/_KeyStats/"
    
    # Check if the directory exists, create if it doesn't
    if not os.path.exists(statspath):
        os.makedirs(statspath)
        print(f"Created directory {statspath}. Please add the necessary ticker files and rerun the script.")
        return
    
    ticker_list = os.listdir(statspath)
    
    # Required on macOS
    if ".DS_Store" in ticker_list:
        os.remove(f"{statspath}/.DS_Store")
        ticker_list.remove(".DS_Store")
    
    # Check if ticker_list is empty
    if not ticker_list:
        print("Ticker list is empty. Please add ticker files to the directory.")
        return
    
    # Print the ticker list for debugging
    print(f"Tickers to download: {ticker_list}")
    
    # Get all Adjusted Close prices for all the tickers in our list,
    # between START_DATE and END_DATE
    all_data = pdr.get_data_yahoo(ticker_list, start=start, end=end)
    
    # Check if data was downloaded successfully
    if all_data.empty:
        print("No data was downloaded. Please check the ticker symbols.")
        return
    
    stock_data = all_data["Adj Close"]
    
    # Remove any columns that hold no data, and print their tickers.
    stock_data.dropna(how="all", axis=1, inplace=True)
    missing_tickers = [
        ticker for ticker in ticker_list if ticker.upper() not in stock_data.columns
    ]
    print(f"{len(missing_tickers)} tickers are missing: \n {missing_tickers} ")
    # If there are only some missing datapoints, forward fill.
    stock_data.ffill(inplace=True)
    stock_data.to_csv("stock_prices.csv")

def build_sp500_dataset(start=START_DATE, end=END_DATE):
    """
    Creates the dataset containing S&P500 prices
    :returns: sp500_index.csv
    """
    index_data = pdr.get_data_yahoo("SPY", start=start, end=end)
    index_data.to_csv("sp500_index.csv")

def build_dataset_iteratively(
    idx_start, idx_end, date_start=START_DATE, date_end=END_DATE
):
    """
    This is an alternative iterative solution to building the stock dataset, which may be necessary if the
    tickerlist is too big.
    Instead of downloading all at once, we download ticker by ticker and append to a dataframe.
    This will download data for tickerlist[idx_start:idx_end], which makes this method suitable
    for chunking data.
    
    :param idx_start: (int) the starting index of the tickerlist
    :param idx_end: (int) the end index of the tickerlist
    """
    
    statspath = "intraQuarter/_KeyStats/"
    
    # Check if the directory exists, create if it doesn't
    if not os.path.exists(statspath):
        os.makedirs(statspath)
        print(f"Created directory {statspath}. Please add the necessary ticker files and rerun the script.")
        return
    
    ticker_list = os.listdir(statspath)
    
    # Check if ticker_list is empty
    if not ticker_list:
        print("Ticker list is empty. Please add ticker files to the directory.")
        return
    
    # Print the ticker list for debugging
    print(f"Tickers to download: {ticker_list}")
    
    df = pd.DataFrame()
    
    for ticker in ticker_list:
        ticker = ticker.upper()
        
        stock_ohlc = pdr.get_data_yahoo(ticker, start=date_start, end=date_end)
        if stock_ohlc.empty:
            print(f"No data for {ticker}")
            continue
        adj_close = stock_ohlc["Adj Close"].rename(ticker)
        df = pd.concat([df, adj_close], axis=1)
    df.to_csv("stock_prices.csv")

if __name__ == "__main__":
    build_stock_dataset()
    build_sp500_dataset()
