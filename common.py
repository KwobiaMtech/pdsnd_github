import pandas as pd
import calendar


def filter_data(df, month, day):
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def default_data(city):
    CITY_DATA = {'chicago': 'chicago.csv',
                 'new york city': 'new_york_city.csv',
                 'washington': 'washington.csv'}
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    # convert date time to month and convert integer value to month name like "January"
    start_month = df['Start Time'].dt.month
    df['month'] = start_month.apply(lambda x: calendar.month_name[x])
    # convert date time to day and convert integer value to day name like "monday"
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['start_hour'] = df['Start Time'].dt.hour
    return df


def load_data(city, month='all', day='all'):
    df = default_data(city)
    df = filter_data(df, month, day)
    return df


def get_column_counts(df, column):
    return df[column].value_counts()


def common_stats(df, column):
    commons = df[column].value_counts().to_dict()
    common = max(commons.keys(), key=(lambda k: commons[k]))
    common_value = max(commons.values())
    return common, common_value


def clean_common_counts(counts):
    counts_dict = counts.to_dict()
    count = max(counts_dict.keys(), key=(lambda k: counts[k]))
    count_value = max(counts_dict.values())
    return count, count_value


def get_data_with_age(df):
    #force copy to avoid warnings
    df = df[pd.notnull(df['Birth Year'])].copy()
    df['Age'] = 2019 - df['Birth Year']
    df['Age'] = df['Age'].astype(int)
    return df

