from datamodules import *

class StockMarketAnalyzer:

    def __init__(self, tickerfolder, watchlistfile):
        """Initialize sub modules"""
        self.dataManager = DataManager(tickerfolder)
        self.watchlistManager = WatchListManager(watchlistfile)

