import datetime

def test_strftime():
    oct21st = datetime.datetime(2021, 10, 21, 16, 29, 0)
    print('oct21st.strftime("%%Y/%%m/%%d %%H:%%M:%%S") = ', oct21st.strftime('%Y/%m/%d %H:%M:%S'))
    print('oct21st.strftime("%%I:%%M %%p") = ', oct21st.strftime('%I:%M %p'))
    print('oct21st.strftime("%%B of \'%%y") = ', oct21st.strftime('%B of \'%y'))

def main():
    test_strftime()

if __name__ == '__main__':
    main()