import pyautogui
# diaplay the mouse cursor's current position
print('Press Ctrl-C to quit.')

try:
    while True:
        # get and print the mouse coordinates
        x,y = pyautogui.position()
        positionStr = 'x: ' + str(x).rjust(4) + ' y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')