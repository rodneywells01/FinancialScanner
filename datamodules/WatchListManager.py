import csv

class WatchListManager:

    def __init__(self, watchlistfile):
        self.tickers = []
        self.watchlistfile = watchlistfile

        # Load saved.
        with open(self.watchlistfile, 'rb') as csvfile:
            reader = csv.reader(csvfile)[0]
            for ticker in reader:
                self.tickers.append(ticker)

            print self.tickers

    def add_ticker(self, ticker):
        """Add a ticker to your watchlist"""

        # Add to local.
        self.tickers.append(ticker)

        # Add to saved.
        with open(self.watchlistfile, 'wb') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(ticker)
