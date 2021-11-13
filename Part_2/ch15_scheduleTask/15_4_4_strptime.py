import datetime

def test_strptime():
    dt = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
    print('datetime.datetime.strptime(\'October 21, 2015\', \'%%B %%d, %%Y\') = ', dt)
    dt = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
    print('datetime.datetime.strptime(\'2015/10/21 16:29:00\', \'%%Y/%%m/%%d %%H:%%M:%S\') = ', dt)
    dt = datetime.datetime.strptime("October of '15", "%B of '%y")
    print('datetime.datetime.strptime("October of \'15", \'%%B of \'%%y\') = ', dt)
    dt = datetime.datetime.strptime("November of '63", "%B of '%y")
    print('datetime.datetime.strptime("November of \'63", \'%%B of \'%%y\') = ', dt)

def main():
    test_strptime()

if __name__ == '__main__':
    main()