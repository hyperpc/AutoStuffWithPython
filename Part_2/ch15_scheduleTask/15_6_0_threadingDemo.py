import threading, time

def takeANap():
    time.sleep(5)
    print('Wake up~')

def main():
    print('Start of main')
    threadObj = threading.Thread(target=takeANap)
    threadObj.start()
    print('End of main')

if __name__ == '__main__':
    main()