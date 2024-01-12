import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

divider = '*'*50

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print("\n")
    print(divider)
    print('👋 Hey! Let\'s explore some U.S. bike share data!')
    print(divider)

    """Collect the city and validate."""
    while True:

        city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
        if city == "":
            print("❌ A city name is required.")
        elif city not in CITY_DATA:
            print("❌ Sorry, we don't have data for that city yet. Choose another? ")
        else:
            print(f"✅ You've chosen \"{city.title()}\".")
            break;

    """Collect the month and validate."""
    while True:
        month = input("Enter a month to filter on (January-June), or leave it blank to select all months. ").lower()
        if month == "":
            print("✅ No input entered, using \"all\"'.")
            month = 'all'
            break
        elif month not in MONTHS:
            print("❌ Sorry, that's not a valid month filter. Choose another? ")
        else:
            print(f"✅ You've chosen \"{month.title()}\".")
            break

    while True:
        day = input("Enter a day of the week to filter on, or leave it blank to select all days. ")
        if day == "":
            print("✅ No input entered, using \"all\"'.")
            day = 'all'
            break
        elif day not in DAYS:
            print("❌ Sorry, that's not a valid day filter. Choose another? ")
        else:
            print(f"✅ You've chosen \"{day.title()}\".")
            break

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

    print(divider)
    print(f"Loading data...")
    print(divider)

    df = pd.read_csv(CITY_DATA[city])

    # clean up
    """We don't want to analyze missing data - drop rows with date NaNs, if they exist."""
    print("Cleaning up the data...")
    df.dropna(subset=['Start Time', 'End Time'], inplace=True)

    """Make sure dates are in the proper format and columns to manipulate."""
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    if month != "all":
        monthIdx = MONTHS.index(month) + 1
        """Need to check both start and end times, since the ride could go over midnight."""
        df = df[(df['Start Time'].dt.month == monthIdx) | (df['End Time'].dt.month == monthIdx)]

    if day != "all":
        dayIdx = DAYS.index(day)
        df = df[(df['Start Time'].dt.dayofweek == dayIdx) | (df['End Time'].dt.dayofweek == dayIdx)]

    print(df.size)
    print(df.head())
    return

def time_stats(df):
    return df

def station_stats(df):
    return df

def trip_duration_stats(df):
    return df

def user_stats(df):
    return df

def main():
    while True:

        try:

            # query for user input
            # city, month, day = get_filters()

            # df = load_data(city, month, day)
            df = load_data("chicago", "march", "all")
            
            # run some analysis
            time_stats(df)
            # station_stats(df)
            # trip_duration_stats(df)
            # user_stats(df)

            # restart the process if the user wants to continue
            restart = input('\nWould you like to run this again? Enter Y or N\n')

            if restart.lower() not in ['yes', 'y']:
                print('✅ Analysis complete. Goodbye!')
                break
        except KeyboardInterrupt:
            print('\n')
            print(divider)
            print("👋 Goodbye!")
            print(divider)
            break
        except Exception as e:
            print(e)
            print('❌ Something funky happened. Try again?')
            break

if __name__ == "__main__":
    main()