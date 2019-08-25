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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Enter a city: ').lower()
            if city in ('chicago', 'new york city', 'washington'):
                print ('That\'s a valid city!')
                break
        except ValueError:
            print('That\'s not valid!')
        else:
            print ('That\'s not a valid city. Please try again!')
        finally:
            print('\nAttempted Input\n')
        
          
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Enter a month: ').lower()
            if month in ('all', 'january', 'february', 'march', 'april', 'may' , 'june'):
                print ('That\'s a valid month!')
                break
        except ValueError:
            print('That\'s not a valid month!')
        else:
            print ('That\'s not a valid month. Please try again!')
        finally:
            print('\nAttempted Input\n')
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Enter a day of week: ').lower()
            if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' , 'sunday'): 
                break
        except ValueError:      
            print('That\'s not a valid day of week!')
        else:
            print ('That\'s not a valid day of week. Please try again!')
        finally:
            print('\nAttempted Input\n')
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
    df['month'] = df ['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour 
    if month !='all':
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
    popular_month =df['month'].mode()[0]
    print ('Most common month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day =df['day_of_week'].mode()[0]
    print ('Most common day: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour=df['hour'].mode()[0]
    print ('Most common hour: ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combination= df.groupby(['Start Station', 'End Station']).size()
    combination1= combination.sort_values(ascending=False).idxmax()
    print('Most frequent combination of Start and End station trip: ', combination1)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df.describe())
    
    sum_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', sum_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

def gender_data(df):
    start_time = time.time()
    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("No data available.")
    
    # TO DO: Display earliest, most recent, and most common year of birth
def birth_year(df):
    start_time = time.time()
    try:
        birth_min = df['Birth Year'].min()
        print ('Earliest year of birth: ', birth_min)
    except:
        print("No data available.")
        
    try:
        birth_max = df['Birth Year'].max()
        print('Most recent year of birth', birth_max)
    except:
        print("No data available.")
        
    try:
        popular_birth_year = df['Birth Year'].value_counts().idxmax()
        print('Most common year of birth: ', popular_birth_year)
    except:
        print("No data available.")
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

    #Display 5 rows of raw data and display the rest of 5 rows if requested
def display_data (df):
    start=0
    end=5
    while True:
        display = input('\nWould you like to display 5 rows of raw data? Enter yes or no.\n')
        if display.lower() == 'yes':
            print (df.iloc[start:end, :])
            start +=5
            end +=5
        elif display.lower() == 'no':
            return
        else:
            print("\nI'm sorry, I'm not sure if you wanted to see more data or not. Let's try again.")
                    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        gender_data(df)
        birth_year(df)
        display_data(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
