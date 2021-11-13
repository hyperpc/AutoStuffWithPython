import datetime, time

def test_timesleep():
    halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
    while datetime.datetime.now() < halloween2016:
        time.sleep(1)

def main():
    test_timesleep()

if __name__ == '__main__':
    main()