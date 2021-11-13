import datetime

def test_timedelta():
    # timedelta
    delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
    print('(delta.days, delta.seconds, delta.microseconds) = ', (delta.days, delta.seconds, delta.microseconds))
    print('delta.total_seconds() = ', delta.total_seconds())
    print('str(delta) = ', str(delta))
    # add days to datetime
    now = datetime.datetime.now()
    print('datetime.datetime.now() = ', now)
    thousandDays = datetime.timedelta(days=1000)
    print('datetime.timedelta(days=1000) = ', thousandDays)
    new_date = now + thousandDays
    print('now + thousandDays = ', new_date)
    print('str(now + thousandDays) = ', str(new_date))
    #
    oct21st = datetime.datetime(2021, 10, 21, 16, 29, 0)
    print('oct21st = ', oct21st)
    aboutThirtyYears = datetime.timedelta(days=365*30)
    print('about 30 years age of oct21st = ', oct21st - aboutThirtyYears)

def main():
    test_timedelta()

if __name__ == '__main__':
    main()