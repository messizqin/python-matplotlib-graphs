def date_format():
    from datetime import datetime
    from matplotlib import pyplot as plt
    from matplotlib import dates as mpl_dates

    plt.style.use("seaborn")

    dates = [datetime(2019, 5, 23),
             datetime(2019, 5, 24),
             datetime(2019, 5, 25),
             datetime(2019, 5, 26),
             datetime(2019, 5, 27),
             datetime(2019, 5, 28),
             datetime(2019, 5, 29)]

    y = [0, 1, 3, 4, 6, 5, 7]

    date_fmt = mpl_dates.DateFormatter("%b, %d %Y")
    plt.gca().xaxis.set_major_formatter(date_fmt)
    plt.gcf().autofmt_xdate()

    plt.plot_date(dates, y, linestyle="solid")

    plt.show()


def date_csv():
    import pandas as pd
    from matplotlib import pyplot as plt
    from matplotlib import dates as mpl_dates
    from pandas.plotting import register_matplotlib_converters

    from Function.edit import Edit

    register_matplotlib_converters()

    plt.style.use("seaborn")

    path = input("please input the date.csv file path here: ")
    data = pd.read_csv(path)

    data["Date"] = Edit.to_datetime(data["Date"])
    data.sort_values("Date", inplace=True)

    price_date = data["Date"]
    price_close = data["Close"]

    plt.plot_date(price_date, price_close, linestyle="solid")

    date_fmt = mpl_dates.DateFormatter("%b, %d %Y")
    plt.gca().xaxis.set_major_formatter(date_fmt)
    plt.gcf().autofmt_xdate()

    plt.title("Bitcoin Prices")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")

    plt.tight_layout()

    plt.show()


date_csv()
