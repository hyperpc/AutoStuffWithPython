import time

def test_round():
    now = time.time()
    print('now = ', now)
    print('round(now) = ', round(now))
    print('round(now, 2) = ', round(now, 2))
    print('round(now, 4) = ', round(now, 4))

def main():
    test_round()

if __name__ == '__main__':
    main()