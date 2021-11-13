import time
import pyperclip

def stopwatchAdv():
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
            #print('Lap #%s: %s (%s)' % (lapNum, totaltime, laptime), end='')
            string_lapNum = str(lapNum).rjust(3)
            string_totaltime = str(totaltime).rjust(8)
            string_laptime = str(laptime).rjust(6)
            output = 'Lap #%s: %s (%s)' % (string_lapNum, string_totaltime, string_laptime)
            pyperclip.copy(output)
            text = pyperclip.paste()
            print(text, end='')
            lapNum += 1
            lasttime = time.time() # reset the last lap time
    except KeyboardInterrupt:
        # handle the Ctrl-C exception to keep its error message from displaying
        print('\nDone!')

def main():
    stopwatchAdv()

if __name__ == '__main__':
    main()