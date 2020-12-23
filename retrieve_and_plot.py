from datetime import date, timedelta

import matplotlib.dates as mpldates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def retrieve_and_plot():
    url = 'https://data.ca.gov/dataset/590188d5-8545-4c93-a9a0-e230f0db7290/resource/926fd08f-cc91-4828-af38-bd45de97f8c3/download/statewide_cases.csv'
    df = pd.read_csv(url)

    # print daily new cases from march 18 to today
    start_date = date.today() - timedelta(days=30)
    end_date = date.today()
    delta = timedelta(days=1)

    df['date'] = pd.to_datetime(df['date'])

    total_cases = 0
    list_daily_new_cases = []
    list_dates = []

    while start_date <= end_date:
        # filter out new cases of the day
        date_filtered = df['date'] == np.datetime64(start_date)

        # add to the grand total and the list
        daily_new_cases =  df[date_filtered]['newcountconfirmed'].sum()
        total_cases += daily_new_cases

        if daily_new_cases == 0:
            break

        # lists for plotting
        list_daily_new_cases.append(daily_new_cases)
        list_dates.append(f"{start_date.month}/{start_date.day}")

        start_date += delta

    # Plot date (daily new cases in the last 30 days)
    # Some styling of the graph
    plt.title('Daily New Cases of COVID-19 in California')
    plt.xlabel('Dates')
    plt.ylabel('Cases')
    plt.grid(axis='y')

    plt.plot(list_dates, list_daily_new_cases, 'r--')

    # Save the file
    plt.savefig('graph.png')

    # Maximize window size and show the plot
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()
    
if __name__ == '__main__':
    retrieve_and_plot()
