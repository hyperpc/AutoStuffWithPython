import time

def stopwatch():
    '''
    A simple stopwatch program.
    '''
    # display the program instructions
    print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch. Press Ctrl+C to quit.')
    input()  # press enter to begin
    print('Started...')
    starttime = time.time() # get the first lap's start time
    lasttime = starttime
    lapNum = 1

    # start tracking the lap time
    try:
        while True:
            input()
            laptime = round(time.time() - lasttime, 2)
            totaltime = round(time.time() - starttime, 2)
            print('Lap #%s: %s (%s)' % (lapNum, totaltime, laptime), end='')
            lapNum += 1
            lasttime = time.time() # reset the last lap time
    except KeyboardInterrupt:
        # handle the Ctrl-C exception to keep its error message from displaying
        print('\nDone!')

def main():
    stopwatch()

if __name__ == '__main__':
    main()