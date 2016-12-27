from datamodules import DataManager as dm
from datamodules import WatchListManager as wlm

class StockMarketAnalyzer:

    def __init__(self, tickerfolder, watchlistfile):
        """Initialize sub modules"""
        self.dataManager = dm.DataManager(tickerfolder)
        self.watchListManager = wlm.WatchListManager(watchlistfile)

        # Get up-to-date data.
        for ticker in self.watchListManager.tickers:
            self.dataManager.fetch_csv(ticker)





