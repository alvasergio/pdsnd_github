import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months = (['all', 'january', 'february', 'march', 'april', 'june'])
    days= ([ 'all', 'monday', 'tusday', 'wensaday', 'thursday', 'friday', 'saturday', 'sunday'])
    print('Hello! let me present you US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        try:
            city= input("Would you like to see data for Chicago, New York City or Washington?:").lower()
            if city in (CITY_DATA.keys()):
                print("you have chosen: {}, city".format(city))
                break
        except KeyError:
                print('That\'s not a valid city name. Try again')
                True
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('what month would you like to filter by? please enter month in full. otherwise enter "all": ').lower()
            if month in months:
                print("Perfect")
                break
        except KeyError:
            print('\nwrong month value. try again please\n')
            True
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Enter wich day to filter by. Please enter day in full, or select "all":').lower()
            if day in days:
                print("Data will be presented in few seconds..." )
                break
        except KeyError:
                print('That\'s not a valid day. Try again please')
                True
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: ',common_month)


    # TO DO: display the most common day of week
    common_day_week = df['day_of_week'].mode()[0]
    print('The most common day of week: ' ,common_day_week)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station: ",common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end sation: ",common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station']+ 'to' + ['End Station']
    common_combination = df['comb'].mode()[0]
    print('The most common combination of start and end:',common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_duration = df['Trip Duration'].sum()
    print('The total travel time is: ',travel_duration)

    # TO DO: display mean travel time
    mean_trip_dur = df['Trip Duration'].mean()
    print('The mean of travel time is: ',mean_trip_dur)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count user types: ")


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The total counts of gender is: ',gender_count)
    else:
        print('The gender count is not available for thsi city')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('The earliest birth year is: ',earliest_year)
        recent_year = df['Birth Year'].max()
        print('The most recent birth year is: ',recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('The most common birth year is: ',common_year)
    else:
        print('Birth Year information is not available for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_statics(df):
    while True:
        x = 0
        y = 5
        dat = input('Enter YES or NO to display the data')
        if dat.lower() == 'yes':
            df = df.iloc[x:y]
            print('Up next the first five rows of the data\n', df)
            x += 1
            y += 1
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_statics(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
