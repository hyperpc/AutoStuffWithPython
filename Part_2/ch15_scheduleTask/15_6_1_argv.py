import threading, time

def threading_argv():
    threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})
    threadObj.start()

def main():
    print('Cats', 'Dogs', 'Frogs', sep=' & ')
    threading_argv()

if __name__ == '__main__':
    main()