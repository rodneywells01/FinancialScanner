import urllib
import datetime


class DataManager:

    def __init__(self, tickerfolder):
        print "Data manager initialized"
        self.start_date = datetime.datetime.now()
        self.end_date = datetime.date(2000, 1, 1)
        self.datalocation = tickerfolder

    def set_start_date(self, startdate):
        self.start_date = startdate

    def set_end_date(self, enddate):
        self.end_date = enddate

    def fetch_market_data(self, ticker):
        """Fetch data from yahoo finance, save in data/"""

        # Construct strings for day, month, and year for start and end.
        startcomponents = ["&d=" + str(self.start_date.month - 1),
                          "&e=" + str(self.start_date.day), "&f=" + str(self.start_date.year)]

        endcomponents = ["&a=" + str(self.end_date.month - 1),
                         "&b=" + str(self.end_date.day), "&c=" + str(self.end_date.year)]

        # Construct url
        url = "http://real-chart.finance.yahoo.com/table.csv?s="
        url += ticker
        for component in startcomponents:
            url += component
        url += "&g=d"
        for component in endcomponents:
            url += component
        url += "&ignore=.csv"
        print url

        # Make request
        urllib.urlretrieve(url, self.datalocation + ticker + ".csv")