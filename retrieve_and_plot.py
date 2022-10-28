from datetime import date, timedelta

import numpy as np
import pandas as pd
import matplotlib.dates as mpldates
import matplotlib.pyplot as plt

def retrieve_and_plot():
    url = 'https://data.chhs.ca.gov/dataset/f333528b-4d38-4814-bebb-12db1f10f535/resource/046cdd2b-31e5-4d34-9ed3-b48cdbc4be7a/download/covid19cases_test.csv'
    df = pd.read_csv(url)

    # Print daily new cases from one month ago to today
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    delta = timedelta(days=1)

    df['date'] = pd.to_datetime(df['date'])

    total_cases = 0
    list_daily_new_cases = []
    list_dates = []

    while start_date <= end_date:
        # filter out new cases of the day
        date_filtered = (df['date'] == np.datetime64(start_date))

        # add to the grand total and the list
        daily_new_cases =  df[date_filtered]['cases'].sum()
        total_cases += daily_new_cases

        if daily_new_cases == 0:
            break

        # lists for plotting
        list_daily_new_cases.append(daily_new_cases)
        list_dates.append(mpldates.date2num(start_date))

        # add one day
        start_date += delta

    # Plot date (daily new cases in the last 30 days)
    # Some styling of the graph
    plt.title('Daily New Cases of COVID-19 in California')
    plt.xlabel('Dates')
    plt.ylabel('Cases')
    plt.grid(axis='y')

    axis = plt.gca()
    axis.set_xticks(axis.get_xticks()[::4])
    axis.xaxis.set_major_locator(mpldates.MonthLocator())
    axis.xaxis.set_major_formatter(mpldates.DateFormatter('%b %d'))
    axis.xaxis.set_major_locator(mpldates.DayLocator(interval=5))
    plt.gcf().autofmt_xdate()

    plt.bar(list_dates, list_daily_new_cases, align='center')

    # Save the file
    plt.savefig(f'images/{date.today().strftime("%Y-%m-%d")}.png')

    # Maximize window size and show the plot
    plt.show()
    
if __name__ == '__main__':
    retrieve_and_plot()
