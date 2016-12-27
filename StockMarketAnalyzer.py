from datamodules import DataManager


class StockMarketAnalyzer:

    def __init__(self, tickerfolder):
        """Initialize sub modules"""
        self.dataManager = DataManager(tickerfolder)
        self.watchlistManager =
