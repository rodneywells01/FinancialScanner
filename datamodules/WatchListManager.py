import csv

class WatchListManager:

    def __init__(self, watchlistfile):
        self.tickers = []
        self.watchlistfile = watchlistfile

        # Load saved.
        with open(self.watchlistfile, 'rbU') as csvfile:
            reader = csv.reader(csvfile)
            for ticker in reader:
                print(ticker)
                self.tickers.append(ticker[0])


    def add_ticker(self, ticker):
        """Add a ticker to your watchlist"""
        if ticker not in self.tickers:
            # Add to local.
            self.tickers.append(ticker)

            # Add to saved.
            with open(self.watchlistfile, 'ab') as csvfile:
                print(ticker)
                writer = csv.writer(csvfile)
                writer.writerow([ticker])
