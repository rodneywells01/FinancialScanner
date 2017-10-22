import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/MU.csv")
    print(df['Adj Close'])
    df[['Close', 'Adj Close']].plot()
    plt.show()


if __name__ == "__main__":
    test_run()
