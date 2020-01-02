import numpy as np
import time
import common as cf


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # common_stats function computes value counts and also returns value counts key
    start_station, start_station_value = cf.common_stats(df, 'Start Station')
    print('The most commonly used start station is {} with a count value of {}'.format(start_station, start_station_value))

    # TO DO: display most commonly used end station
    end_station, end_station_value = cf.common_stats(df, 'End Station')
    print('The most commonly used end station is {} with a count value of {}'.format(end_station,
                                                                                       end_station_value))

    # print(end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_station_counts = cf.get_column_counts(df, 'Start Station')
    end_station_counts = cf.get_column_counts(df, 'End Station')
    final = start_station_counts + end_station_counts
    common_combined, common_combined_value = cf.clean_common_counts(final)
    # print(common_combined)
    print('The most commonly used end and start station  is {} with a combined count value of {}'.format(common_combined,
                                                                                       common_combined_value))

    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    #df = cf.get_data_with_age(df)
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = cf.get_column_counts(df, 'User Type').to_dict()
    print('{} has the following user type details '.format(city))

    for i in user_types:
        if user_types[i] == 1:
            print('{} {}'.format(user_types[i], i))
        else:
            print('{} {}s'.format(user_types[i], i))

    print()

    # washington data do not contain Birth Year
    print()
    if city == 'chicago' or city == 'new york city':

        print('\nCalculating User Age  Stats...\n')
        user_ages = cf.get_column_counts(cf.get_data_with_age(df), 'User Type').to_dict()

        for i in user_ages:
            # get data with age
            if user_types[i] == 1:
                df_age = cf.get_data_with_age(df)
                df_age = df_age[df_age['User Type'] == i]
                common_age, common_age_value = cf.common_stats(df_age, 'Age')
                print('{} had only {}s with a common occurring age of about {}years'.format(city, i, common_age))
                return
            else:
                df_age = cf.get_data_with_age(df)
                df_age = df_age[df_age['User Type'] == i]
                common_age, common_age_value = cf.common_stats(df_age, 'Age')
                print('The frequent {} is about {} years old'.format(i, common_age))

        # TO DO: Display counts of gender
        print()
        print('Below are some gender stats you will be interested in ')
        gender = cf.get_column_counts(df, 'Gender').to_dict()

        print('{} riders were {}s whiles {} riders were {}s'.format(list(gender.values())[0], list(gender.keys())[0],
                                                                    list(gender.values())[1], list(gender.keys())[1]))

        # TO DO: Display earliest, most recent, and most common year of birth
        # common_stats function computes value counts and also returns value counts key
        year, common_year_value = cf.common_stats(df, 'Birth Year')
        common_year = str(int(year))

        df.sort_values("Birth Year", axis=0, ascending=False,
                       inplace=True, na_position='last')
        most_recent_birth_year = str(int(df.iloc[0]['Birth Year']))
        df = df[np.isfinite(df['Birth Year'])]
        earliest_birth_year = str(int(df.iloc[-1]['Birth Year']))

        print('The common occurring year is {} with a counts of {} whiles the most '
              'recent year is {} as well as earliest year occurring at {}'
              .format(common_year, common_year_value, most_recent_birth_year, earliest_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def show_sample_data(df,show_data):
    """Displays statistics on the most frequent times of travel."""

    if show_data == 'yes':
        print('\nShowing sample data ...\n')
        start_time = time.time()

        print(df.head(5))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # common_stats function computes value counts and also returns value counts key
    common_month, common_month_value = cf.common_stats(df, 'month')

    print('The most common occurring month is {} with a count of {}'.format(common_month, common_month_value))

    # TO DO: display the most common day of week
    common_week, common_week_value = cf.common_stats(df, 'day_of_week')
    print('The most common occurring day of the week is {} with a count of {}'.format(common_week, common_week_value))

    # TO DO: display the most common start hour
    common_hour, common_hour_value = cf.common_stats(df, 'start_hour')
    print('The most common starting hour is {} with a count of {}'.format(common_hour, common_hour_value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum(axis=0, skipna=True) / 3600
    # print(total_travel_time)
    print('Total time travel  in minutes is about {}mins'.format(np.ceil(total_travel_time)))

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean(axis=0, skipna=True)
    # print(mean_travel_time)
    print('Mean travel time in seconds is about {}sec'.format(np.ceil(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def get_filters():
    cities = ['chicago', 'new york city', 'washington']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    raw_response = ['yes', 'no']

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Which city(chicago,new york city,washington) would you like to explore? ")
    while city not in cities:
        city = input("Please ensure you entered the right city(chicago,new york city,washington): ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please enter month (all,June,May,April,February,March,January): ")
    while month not in months:
        month = input("Please ensure you entered the right month(all,June,May,April,February,March,January): ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter day (all, monday, tuesday, ... sunday): ")
    while day not in days:
        day = input("Please ensure you entered the right day(all, monday, tuesday, ... sunday): ")

    raw_data = input("Would you like to see 5 line sample raw data.Type yes or no): ")
    while raw_data not in raw_response:
        raw_data = input("Please enter yes or no ")

    print('-' * 40)
    return city.lower(), month, day, raw_data

