import pandas as pd
import os
datastring = "http://real-chart.finance.yahoo.com/table.csv?s=MSFT&d=4&e=29&f=2016&g=d&a=2&b=13&c=1986&ignore=.csv"

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read Stock data (adjusted close) for given symbols from csv files"""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df =  df.join(df_temp,  how='inner')

    return df

def test():
    start_date = '2016-02-22'
    end_date = '2016-02-26'
    dates = pd.date_range(start_date, end_date) # Wow, can't believe this function exists
                                                # Creates a list of dates in this range.
    # Empty dataframe
    dataframe1 = pd.DataFrame(index=dates) # datetimeindex object creation

    # Read MU
    """
    dfMU = pd.read_csv("data/MU.csv",
                       index_col="Date",
                       parse_dates=True,
                       usecols=['Date', 'Adj Close'], # Specify desired cols
                       na_values=['nan'] # nan string should be interpreted as nan
                       )

    # Join the two data frames using Dataframe.join
    """
    """
    dataframe1 = dataframe1.join(dfMU)
    dataframe1 = dataframe1.dropna() # drop all dates that are nan
    """

    """
    # The above, in one line:
    dataframe1 = dataframe1.join(dfMU, how='inner')
    """
    symbols = ['XON', 'NFLX', 'MSFT']

    for symbol in symbols:
        df_temp = pd.read_csv("data/" + symbol + ".csv", index_col="Date", parse_dates=True,
                              usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        dataframe1 =  dataframe1.join(df_temp)

    return dataframe1

if __name__ == "__main__":
    #df = test()
    symbols = ["MU", "XON", "GME", "TSLA"]
    start_date = '2016-02-22'
    end_date = '2016-03-26'
    dates = pd.date_range(start_date, end_date)
    df = get_data(symbols, dates)
    print df