from datamodules import DataManager as dm
from datamodules import WatchListManager as wlm

class StockMarketAnalyzer:

    def __init__(self, tickerfolder, watchlistfile):
        """Initialize sub modules"""
        self.dataManager = dm.DataManager(tickerfolder)
        self.watchListManager = wlm.WatchListManager(watchlistfile)

        # Get up-to-date data.
        print("Fetching up to date data...")
        tickercounter = 1
        for ticker in self.watchListManager.tickers:
            print("Fetching... (" + str(tickercounter) + " / " + str(len(self.watchListManager.tickers)) + ")")
            self.dataManager.fetch_market_data(ticker)
            tickercounter  += 1