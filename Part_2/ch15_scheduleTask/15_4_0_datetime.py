import datetime, time

def test_datetime():
    now = datetime.datetime.now()
    print('datetime.datetime.now() = ', now)
    dt = datetime.datetime(2021, 11, 13, 12, 56, 19)
    print('(dt.year, dt.month, dt.day) = ', (dt.year, dt.month, dt.day))
    print('dt.year, dt.month, dt.day = ', dt.year, dt.month, dt.day)
    print('dt.hour, dt.minute, dt.second = ', dt.hour, dt.minute, dt.second)

    datetimeFromTimestamp = datetime.datetime.fromtimestamp(1000000)
    print('datetime.datetime.fromtimestamp(1000000) = ', datetimeFromTimestamp)
    datetimeFromTimenow = datetime.datetime.fromtimestamp(time.time())
    print('datetime.datetime.fromtimestamp(time.time()) = ', datetimeFromTimenow)

    print('(now == datetimeFromTimenow) = ', (now == datetimeFromTimenow))
    print('(now > datetimeFromTimenow) = ', (now > datetimeFromTimenow))
    print('(now < datetimeFromTimenow) = ', (now < datetimeFromTimenow))

def main():
    test_datetime()

if __name__ == '__main__':
    main()