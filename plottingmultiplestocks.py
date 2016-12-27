import os
import pandas as pd
import matplotlib.pyplot as plt
import urllib
import datetime

def fetch_ticker(ticker):
    # Get current month, day, and year.
    now = datetime.datetime.now()
    print now.month, now.day, now.year
    datecomponents = ["&d=" + str(now.month - 1), "&e=" + str(now.day), "&f=" + str(now.year)]

    url = "http://real-chart.finance.yahoo.com/table.csv?s="
    url += ticker
    for component in datecomponents:
        url += component

    url += "&g=d&a=2&b=13&c=1986&ignore=.csv"
    print url
    urllib.urlretrieve(url, "data\\" + ticker + ".csv")

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def normalize_data(df):
    """normalize stock prices using first row of database"""
    return df/df.ix[0, :]

def get_data(symbols, dates):
    """Read Stock data (adjusted close) for given symbols from csv files"""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        path = symbol_to_path(symbol)
        if os.path.isfile(path) == False:
            print symbol + " not found. Fetching remotely."
            fetch_ticker(symbol)
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        #if df_temp == False:
        #    print "FILE NOT FOUND!"
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df_temp = normalize_data(df_temp) #TODO: WHAT THE HECK

        df = df.join(df_temp,  how='inner')

    return df


def plot_data(df, title="Stock Prices"):
    """Plot stock Prices"""
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


if __name__ == "__main__":
    symbols = ["MU", "XON", "GME", "TSLA"]

    update = True
    if update:
        print "Updating stocks"
        for symbol in symbols:
            fetch_ticker(symbol)

    print "Update complete"

    start_date = '2016-01-01'
    end_date = '2016-05-26'
    dates = pd.date_range(start_date, end_date)
    df = get_data(symbols, dates)
    plot_data(df)
    # fetch_ticker("SUNE")
