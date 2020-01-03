import common as cf
import main_stat as ms


def main():
    while True:
        city, month, day, raw_data = ms.new_get_filters()
        df = cf.load_data(city, month, day)

        ms.show_sample_data(df, raw_data)
        # using default_data function help to get data without filtering month and day
        ms.time_stats(cf.default_data(city))
        ms.station_stats(df)
        ms.trip_duration_stats(df)
        ms.user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()




